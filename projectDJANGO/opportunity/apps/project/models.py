from django.db import models
from django.conf import settings


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


class areaInteresse(models.Model):
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    interesseProfessor = models.CharField(max_length=255)

    def __str__(self):
        return self.interesseProfessor


class Aluno(models.Model):
    matriculaAluno = models.CharField(max_length=255)
    dataIngresso = models.DateField()
    nomeAluno = models.CharField(max_length=255)
    periodo = models.IntegerField()
    CRA = models.FloatField()
    dataEstimadaSaida = models.DateField()

    def __str__(self):
        return self.nomeAluno


class Inscricao(models.Model):
    IDAluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    IDVAGA = models.ForeignKey(vagasEmprego, on_delete=models.CASCADE)
