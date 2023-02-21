from accounts.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Professor(models.Model):
    nomeProfessor = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Professor(a)'
        verbose_name_plural = 'Professores(as)'

    def __str__(self):
        return self.nomeProfessor


class vagasEmprego(models.Model):
    nivel = (
        ('B', 'Basico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    numeroVagas = models.IntegerField("Número de vagas")
    nivel = models.CharField(
        max_length=1, choices=nivel)
    horasSemana = models.IntegerField("Horas Semana")
    valorSalario = models.FloatField("Valor Salario")
    dataCadastro = models.DateField("Data de cadastro", default=timezone.now)
    tipoVaga = models.CharField("Tipo da Vaga", max_length=255)
    beneficios = models.CharField("Beneficios", max_length=255)
    tituloVaga = models.CharField("Titulo da Vaga", max_length=255)
    descricao = models.TextField("Descrição")
    dataFechamento = models.DateField("Data de Fechamento")
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return self.tituloVaga + ' - ' + str(self.nivel)
