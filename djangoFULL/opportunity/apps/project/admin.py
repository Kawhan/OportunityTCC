from django.contrib import admin

from .models import Professor, vagasEmprego


# Register your models here.
@admin.register(vagasEmprego)
class VagasEmpregoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tituloVaga',
        'numeroVagas',
        'nivel',
        'horasSemana',
        'valorSalario',
        'dataCadastro',
        'dataFechamento'
    )

    search_fields = (
        'tituloVaga',
        'numeroVagas',
        'nivel',
        'horasSemana',
        'valorSalario',
        'dataCadastro',
        'dataFechamento'
    )
    list_display_links = ['id', 'nivel']
    # list_editable = ['', ]
    list_per_page = 20

    pass


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'nomeProfessor',
    )

    pass
