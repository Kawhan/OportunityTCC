from django.contrib import admin
from .models import Aluno, areaInteresse, Inscricao, Professor,vagasEmprego

# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'nomeAluno',
        'matriculaAluno',
        'periodo',
        'CRA'
    )
    
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nomeProfessor',
    )
    

@admin.register(vagasEmprego)
class VagasEmpregoAdmin(admin.ModelAdmin):
    list_display = (
        'tituloVaga',
        'numeroVagas',
        'nivel',
        'horasSemana',
        'valorSalario',
        'dataCadastro',
        'dataFechamento'
    )

@admin.register(areaInteresse)
class areaInteresseAdmin(admin.ModelAdmin):
    list_display = (
        'professor_id',
        'interesseProfessor'
    )

@admin.register(Inscricao)
class Inscricao(admin.ModelAdmin):
    list_display = (
        'IDAluno',
        'IDVAGA'
    )