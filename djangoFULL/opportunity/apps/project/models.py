from django.db import models


# Create your models here.
class Professor(models.Model):
    nomeProfessor = models.CharField(max_length=255)

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

    numeroVagas = models.IntegerField()
    nivel = models.CharField(
        max_length=1, choices=nivel)
    horasSemana = models.IntegerField()
    valorSalario = models.FloatField()
    dataCadastro = models.DateField()
    tipoVaga = models.CharField(max_length=255)
    beneficios = models.CharField(max_length=255)
    tituloVaga = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    dataFechamento = models.DateField()
    professor_id = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return self.tituloVaga + ' - ' + str(self.nivel)
