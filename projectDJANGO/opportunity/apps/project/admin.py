from django.contrib import admin
from django.contrib.admin.options import TabularInline

from .models import (Aluno, Inscricao, Professor, areaInteresse,
                     professorComposto, vagasEmprego)

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


# @admin.register(usuarioComposto)
# class usuarioCompostoAdmin(admin.ModelAdmin):
#     list_display = (
#         'nome_aluno',
#         'username_user'
#     )

#     def nome_aluno(self, obj):
#         return obj.id_aluno.nomeAluno

#     def username_user(self, obj):
#         return obj.id_user_aluno.username

#     pass


@admin.register(professorComposto)
class professorCompostoAdmin(admin.ModelAdmin):
    list_display = (
        'nome_professor',
        'username_user'
    )

    def nome_professor(self, obj):
        return obj.id_professor.nomeProfessor

    def username_user(self, obj):
        return obj.id_user_professor.username
