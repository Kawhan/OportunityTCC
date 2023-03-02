import datetime

from accounts.models import User, UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from project.forms import JobForm
from project.models import Professor, vagasEmprego


# View of vagas
@login_required
def index(request):
    vagas = vagasEmprego.objects.all().filter(
        disponivel='S').order_by('-dataFechamento')

    user = request.user
    user_info = None

    aluno = get_object_or_404(UserProfile, user=user)

    if user.user_is_teacher:
        user_info = Professor.objects.filter(user=request.user.id).first()
    else:
        user_info = get_object_or_404(UserProfile, user=user)

    paginator = Paginator(vagas, 6)
    page = request.GET.get('page')
    vagas_per_page = paginator.get_page(page)

    dados = {}

    dados['vagas'] = vagas_per_page
    dados['title'] = "Home"
    dados['user'] = user
    dados['user_info'] = user_info

    return render(request, 'project/index.html', dados)


@login_required
def view_vaga(request, vaga_id):
    vaga = get_object_or_404(
        vagasEmprego.objects.select_related('professor'), id=vaga_id)

    dados = {}

    dados['vaga'] = vaga
    dados['title'] = 'Visualizar vaga'

    return render(request, 'project/view_vaga.html', dados)


@login_required
def create_vaga(request):
    if not request.user.user_is_teacher:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    context = {}
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    user = Professor.objects.filter(user=request.user.id).first()

    # print(user)

    form = JobForm(request.POST or None, initial={
                   "professor": user, "dataCadastro": date})

    if form.is_valid():
        # print('passou')
        form.save()
        return redirect('minhas_vagas')

    context['form'] = form
    context['professor'] = user
    context['title'] = "Cadastrar vagas"

    return render(request, 'project/forms.html', context)


@login_required
def change_vaga(request, vaga_id):
    if not request.user.user_is_teacher:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    nome = request.user

    context = {}
    job = get_object_or_404(vagasEmprego, pk=vaga_id)
    job.dataCadastro = job.dataCadastro.strftime('%Y-%m-%d')
    job.dataFechamento = job.dataFechamento.strftime('%Y-%m-%d')

    if job.professor.user != nome:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    form = JobForm(request.POST or None, instance=job)

    if form.is_valid():
        # print(form.id)

        form.save()
        messages.success(request, "Vaga de emprego alterado com sucesso!")
        return redirect('minhas_vagas')

    context["form"] = form
    context["title"] = "Alterar vaga"

    return render(request, "project/forms.html", context)


@login_required
def search(request):

    # print('teste')
    vagas = vagasEmprego.objects.all().filter(
        disponivel='S').order_by('-dataFechamento')

    user = request.user
    user_info = None

    if user.user_is_teacher:
        user_info = Professor.objects.filter(user=request.user.id).first()
    else:
        user_info = get_object_or_404(UserProfile, user=user)

    if 'search' in request.GET:
        search_name = request.GET['search']
        if search_name:
            vagas = vagas.filter(tituloVaga__icontains=search_name)

    dados = {
        'vagas': vagas,
        'title': 'Filtrar vagas',
        'user': user,
        'user_info': user_info
    }

    return render(request, 'project/search.html', dados)


@login_required
def delete_job(request, vaga_id):
    if not request.user.user_is_teacher:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    nome = request.user

    context = {}
    job = get_object_or_404(vagasEmprego, pk=vaga_id)
    context['title'] = 'Deletar vaga'
    context['vaga'] = job

    if job.professor.user != nome:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    if request.method == "POST":
        job.delete()
        return redirect('minhas_vagas')

    return render(request, 'project/delete.html', context)


@login_required
def minhas_vagas(request):
    if not request.user.user_is_teacher:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    professor = Professor.objects.filter(user=request.user.id).first()

    vagas = vagasEmprego.objects.all().filter(
        professor=professor).order_by('-dataFechamento')

    paginator = Paginator(vagas, 6)
    page = request.GET.get('page')
    vagas_per_page = paginator.get_page(page)

    dados = {}

    dados['vagas'] = vagas_per_page
    dados['title'] = "Minhas oportunidades"

    return render(request, 'project/dashboard.html', dados)


@login_required
def inscrever_aluno(request, vaga_id):
    data_hoje = datetime.datetime.today().date()

    if request.user.user_is_teacher:
        messages.error(
            request, "Você não pode realizar essa operação! Por ser professor")
        return redirect("index")

    user = request.user.id

    aluno = get_object_or_404(UserProfile, user=user)

    if aluno == None:
        messages.error(request, "Erro você não é aluno")
        return redirect("index")

    job = get_object_or_404(vagasEmprego, pk=vaga_id)

    if aluno in job.aluno.all():
        messages.error(request, "Você já está inscrito nessa vaga")
        return redirect("index")

    if job == None:
        messages.error(request, "Vaga não existe!")
        return redirect("index")

    if data_hoje > job.dataFechamento:
        messages.error(request, "Vaga não está aberta!")
        return redirect("index")

    job.aluno.add(aluno)

    messages.success(request, "interesse registrado com sucesso!")
    return redirect('index')


@login_required
def desinscrever_aluno(request, vaga_id):
    if request.user.user_is_teacher:
        messages.error(
            request, "Você não pode realizar essa operação! Por ser professor")
        return redirect("index")

    user = request.user.id

    aluno = get_object_or_404(UserProfile, user=user)

    if aluno == None:
        messages.error(request, "Erro você não é aluno")
        return redirect("index")

    job = get_object_or_404(vagasEmprego, pk=vaga_id)

    data_hoje = datetime.datetime.today().date()

    if data_hoje > job.dataFechamento:
        messages.error(request, "Vaga não está aberta!")
        return redirect("index")

    if aluno in job.aluno.all():
        job = get_object_or_404(vagasEmprego, pk=vaga_id)

        if job == None:
            messages.error(request, "Vaga não existe!")
            return redirect("index")

        job.aluno.remove(aluno)

        job.save()

        messages.success(request, "Seu interesse foi removido com sucesso!")

        return redirect("index")

    messages.error(request, "Você não possui interesse nessa vaga!")
    return redirect('index')


@login_required
def projeto_pesquisa(request):
    vagas = vagasEmprego.objects.all().filter(
        disponivel='S').filter(tipo_vaga='PP').order_by('-dataFechamento')

    user = request.user
    user_info = None

    aluno = get_object_or_404(UserProfile, user=user)

    if user.user_is_teacher:
        user_info = Professor.objects.filter(user=request.user.id).first()
    else:
        user_info = get_object_or_404(UserProfile, user=user)

    paginator = Paginator(vagas, 6)
    page = request.GET.get('page')
    vagas_per_page = paginator.get_page(page)

    dados = {}

    dados['vagas'] = vagas_per_page
    dados['title'] = "Home"
    dados['user'] = user
    dados['user_info'] = user_info

    return render(request, 'project/pesquisa.html', dados)


@login_required
def projeto_extencao(request):
    vagas = vagasEmprego.objects.filter(
        disponivel='S').filter(tipo_vaga='PE').order_by('-dataFechamento')

    user = request.user
    user_info = None

    aluno = get_object_or_404(UserProfile, user=user)

    if user.user_is_teacher:
        user_info = Professor.objects.filter(user=request.user.id).first()
    else:
        user_info = get_object_or_404(UserProfile, user=user)

    paginator = Paginator(vagas, 6)
    page = request.GET.get('page')
    vagas_per_page = paginator.get_page(page)

    dados = {}

    dados['vagas'] = vagas_per_page
    dados['title'] = "Home"
    dados['user'] = user
    dados['user_info'] = user_info

    return render(request, 'project/pesquisa.html', dados)


@login_required
def estagio(request):
    vagas = vagasEmprego.objects.filter(
        disponivel='S').filter(tipo_vaga='ES').order_by('-dataFechamento')

    user = request.user
    user_info = None

    aluno = get_object_or_404(UserProfile, user=user)

    if user.user_is_teacher:
        user_info = Professor.objects.filter(user=request.user.id).first()
    else:
        user_info = get_object_or_404(UserProfile, user=user)

    paginator = Paginator(vagas, 6)
    page = request.GET.get('page')
    vagas_per_page = paginator.get_page(page)

    dados = {}

    dados['vagas'] = vagas_per_page
    dados['title'] = "Home"
    dados['user'] = user
    dados['user_info'] = user_info

    return render(request, 'project/estagio.html', dados)
