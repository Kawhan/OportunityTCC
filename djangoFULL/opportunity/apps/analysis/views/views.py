from accounts.models import UserProfile
from analysis.data.grafics import Start
from django.shortcuts import render
from project.models import vagasEmprego

# Create your views here.


def analises(request):
    alunos_pesquisa = []
    alunos_extensao = []
    alunos_estagio = []

    labels = []
    data = {}
    data = Start.define_data_info(data)
    data = Start.define_info_count_from_jobs(data)

    query_set_data = {}

    query_set_data = Start.query_set_info_from_jobs(query_set_data)

    # Quantidade alunos inscritos em pesquisas
    alunos_pesquisa = Start.cal_info_stundents_in_research_project(
        query_set_data, alunos_pesquisa, data)['alunos_pesquisa']
    data = Start.cal_info_stundents_in_research_project(
        query_set_data, alunos_pesquisa, data)['data']
    data = Start.all_subscribe_in_research_project(
        query_set_data, alunos_pesquisa, data)['data']

    # Quntidade alunos inscritos em extensão
    alunos_extensao = Start.cal_info_students_in_extension_project(
        query_set_data, alunos_extensao, data)['alunos_extensao']
    data = Start.cal_info_students_in_extension_project(
        query_set_data, alunos_extensao, data)['data']
    data = Start.all_subscribe_in_extesion_project(
        query_set_data, alunos_extensao, data)['data']

    #  Quantidade alunos em estágio
    alunos_estagio = Start.cal_info_students_in_intern(
        query_set_data, alunos_estagio, data)['alunos_estagio']
    data = Start.cal_info_students_in_intern(
        query_set_data, alunos_estagio, data)['data']
    data = Start.all_subscribe_in_intern(
        query_set_data, alunos_estagio, data)['data']

    # Quantidade inscritos em pesquisa

    return render(request, "analises/analises.html", {
        'labels': labels,
        'data': data
    })
