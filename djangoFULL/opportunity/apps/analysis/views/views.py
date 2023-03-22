from accounts.models import UserProfile
from analysis.data.grafics import IndividualStart, Start
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from project.models import vagasEmprego

# Create your views here.


def analises(request):
    if not request.user.user_is_teacher:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

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

    return render(request, "analises/analises.html", {
        'title': "Analises gerais",
        'labels': labels,
        'data': data
    })


def indiviual_analysis(request, vaga_id):
    if not request.user.user_is_teacher:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    nome = request.user
    job = get_object_or_404(vagasEmprego, pk=vaga_id)

    if job.professor.user != nome:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    alunos = []

    data = {}
    data = IndividualStart.define_data_info(data)
    data = IndividualStart.define_info_count_from_jobs(data, vaga_id)

    # catch stundents in job
    alunos = IndividualStart.info_subscribe_in_job(data, alunos)['alunos']
    data = IndividualStart.info_subscribe_in_job(data, alunos)['data']

    if data == False:
        messages.error(
            request, "A vaga não tem nenhum inscrito, por favor aguardar")
        return redirect("minhas_vagas")

    return render(request, "analises/individual.html", {
        'title': 'Graficos',
        'data': data
    })
