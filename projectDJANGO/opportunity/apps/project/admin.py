from django.contrib import admin
from .models import Aluno, areaInteresse, Inscricao, Professor, vagasEmprego
from django.contrib.admin.options import TabularInline

# Register your models here.


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'nomeAluno',
        'matriculaAluno',
        'periodo',
        'CRA'
    )

    pass


class areaInteresseAdminInline(TabularInline):
    model = areaInteresse
    extra = 1

    pass


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nomeProfessor',
    )
    inlines = [
        areaInteresseAdminInline,
    ]

    pass


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

    pass


@admin.register(Inscricao)
class Inscricao(admin.ModelAdmin):
    list_display = (
        'IDAluno',
        'IDVAGA'
    )

    pass
