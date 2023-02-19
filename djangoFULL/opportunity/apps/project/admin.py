from django.contrib import admin

from .models import Professor, vagasEmprego


# Register your models here.
@admin.register(vagasEmprego)
class VagasEmpregoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['tituloVaga', 'numeroVagas']}),
        ("Content", {"fields": [
         'nivel', 'horasSemana', 'valorSalario', 'descricao']}),
        ("Date", {"fields": ['dataCadastro', 'dataFechamento']}),
        ("Keys", {"fields": ['professor']})

    ]

    list_display = (
        'id',
        'tituloVaga',
        'numeroVagas',
        'nivel',
        'horasSemana',
        'valorSalario',
        'dataCadastro',
        'dataFechamento',
        'professor'
    )

    search_fields = (
        'tituloVaga',
        'numeroVagas',
        'nivel',
        'horasSemana',
        'valorSalario',
        'dataCadastro',
        'dataFechamento',
        'professor__nomeProfessor'
    )

    list_filter = (
        'nivel',
        'horasSemana',
        'dataCadastro',
        'professor_id__nomeProfessor',
        'numeroVagas'
    )

    list_display_links = ['id', 'nivel']

    def nome_professor(self, obj):
        return obj.professor.nomeProfessor

    # list_editable = ['', ]
    list_per_page = 20

    pass


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nomeProfessor',
    )

    pass
