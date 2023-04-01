from datetime import date

from accounts.models import User, UserProfile
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


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

    disponivel = (
        ('S', 'Sim'),
        ('N', 'Não')
    )

    tipo_vaga = {
        ('PP', 'Projeto de Pesquisa'),
        ('PE', 'Projeto de extensão'),
        ('ES', 'Estágio'),
    }

    numeroVagas = models.IntegerField("Número de vagas")
    horasSemana = models.IntegerField("Horas Semana")
    valorSalario = models.FloatField("Valor Salario")
    dataCadastro = models.DateField("Data de cadastro", default=timezone.now)
    beneficios = models.CharField("Beneficios", max_length=255)
    tituloVaga = models.CharField("Titulo da Vaga", max_length=255)
    # descricao = HTMLField("Descrição")
    pdf = models.FileField(upload_to='pdfs/%d/%m/%Y/')
    dataFechamento = models.DateField("Data de Fechamento")
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    aluno = models.ManyToManyField(
        UserProfile, blank=True)
    disponivel = models.CharField(max_length=1, choices=disponivel)
    tipo_vaga = models.CharField(max_length=2, choices=tipo_vaga)
    nome_empresa = models.CharField(
        "Nome empresa ou nome projeto", max_length=255)
    link_vaga = models.CharField("Link da vaga", max_length=255)

    @property
    def is_closed(self):
        return date.today() > self.dataFechamento

    def __str__(self):
        return self.tituloVaga + ' - ' + str(self.nivel)
