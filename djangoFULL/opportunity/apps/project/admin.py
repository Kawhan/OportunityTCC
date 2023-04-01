from django.contrib import admin

from .models import Professor, vagasEmprego


# Register your models here.
@admin.register(vagasEmprego)
class VagasEmpregoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['tituloVaga', 'numeroVagas']}),
        ("Content", {"fields": [
            'horasSemana', 'valorSalario', 'beneficios', 'tipo_vaga']}),
        ("Date", {"fields": ['dataCadastro', 'dataFechamento']}),
        ("Alunos Inscritos", {"fields": ['aluno']})

    ]

    list_display = (
        'id',
        'tituloVaga',
        'numeroVagas',
        'horasSemana',
        'valorSalario',
        'dataCadastro',
        'dataFechamento',
        'professor',
        'tipo_vaga'
    )

    search_fields = (
        'tituloVaga',
        'numeroVagas',
        'horasSemana',
        'valorSalario',
        'dataCadastro',
        'dataFechamento',
        'professor__nomeProfessor'
    )

    list_filter = (
        'horasSemana',
        'dataCadastro',
        'professor_id__nomeProfessor',
        'numeroVagas'
    )

    list_display_links = ['id']

    def nome_professor(self, obj):
        return obj.professor.nomeProfessor

    # list_editable = ['', ]
    list_per_page = 5

    pass


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nomeProfessor',
    )

    pass
