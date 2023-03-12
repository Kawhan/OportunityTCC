from accounts.models import UserProfile
from django.shortcuts import render
from project.models import vagasEmprego

# Create your views here.


def analises(request):
    alunos_pesquisa = []
    alunos_extensao = []
    alunos_estagio = []

    labels = []
    data = {}
    data['alunos_SI_pesquisa'] = 0
    data['alunos_LCC_pesquisa'] = 0

    data['inscricoes_SI_pesquisa'] = 0
    data['inscricoes_LCC_pesquisa'] = 0

    data['alunos_SI_extensao'] = 0
    data['alunos_LCC_extensao'] = 0

    data['alunos_SI_estagio'] = 0
    data['alunos_LCC_estagio'] = 0

    queryset = vagasEmprego.objects.all()
    data['PP'] = vagasEmprego.objects.filter(tipo_vaga='PP').count()
    data['PE'] = vagasEmprego.objects.filter(tipo_vaga='PE').count()
    data['ES'] = vagasEmprego.objects.filter(tipo_vaga='ES').count()

    queryset_pesquisa = vagasEmprego.objects.filter(tipo_vaga='PP')

    queryset_extensao = vagasEmprego.objects.filter(tipo_vaga='PE')

    queryset_estagio = vagasEmprego.objects.filter(tipo_vaga='ES')

    # Quantidade alunos inscritos em pesquisas
    for pesquisa in queryset_pesquisa:
        for aluno in pesquisa.aluno.values().distinct():
            if aluno['curso'] == 'SI' and aluno not in alunos_pesquisa:
                alunos_pesquisa.append(aluno)
                data['alunos_SI_pesquisa'] += 1
            if aluno['curso'] == 'LCC' and aluno not in alunos_pesquisa:
                alunos_pesquisa.append(aluno)
                data['alunos_LCC_pesquisa'] += 1
            if aluno['curso'] == 'SI':
                data['inscricoes_SI_pesquisa'] += 1
            if aluno['curso'] == 'LCC':
                data['inscricoes_LCC_pesquisa'] += 1

    # Quntidade alunos inscritos em extensão
    for extensao in queryset_extensao:
        for aluno in extensao.aluno.values().distinct():
            if aluno['curso'] == 'SI' and aluno not in alunos_extensao:
                alunos_extensao.append(aluno)
                data['alunos_SI_extensao'] += 1
            elif aluno['curso'] == 'LCC' and aluno not in alunos_extensao:
                alunos_extensao.append(aluno)
                data['alunos_LCC_extensao'] += 1

    #  Quantidade alunos em estágio
    for estagio in queryset_estagio:
        for aluno in estagio.aluno.values().distinct():
            if aluno['curso'] == 'SI' and aluno not in alunos_estagio:
                alunos_estagio.append(aluno)
                data['alunos_SI_estagio'] += 1
            elif aluno['curso'] == 'LCC' and aluno not in alunos_estagio:
                alunos_estagio.append(aluno)
                data['alunos_LCC_estagio'] += 1

        # data['alunos_SI_pesquisa'] = pesquisa.aluno.filter()
        # data['alunos_LCC_pesquisa'] = pesquisa.aluno.filter()

    # Quantidade inscritos em pesquisa

    return render(request, "analises/analises.html", {
        'labels': labels,
        'data': data
    })
