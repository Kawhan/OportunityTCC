import datetime

from accounts.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from project.forms import JobForm
from project.models import Professor, vagasEmprego


# View of vagas
@login_required
def index(request):
    vagas = vagasEmprego.objects.all().order_by('-dataCadastro')

    paginator = Paginator(vagas, 3)
    page = request.GET.get('page')
    vagas_per_page = paginator.get_page(page)

    dados = {}

    dados['vagas'] = vagas_per_page
    dados['title'] = "Home"

    return render(request, 'project/index.html', dados)


@login_required
def view_vaga(request, vaga_id):
    vaga = get_object_or_404(
        vagasEmprego.objects.select_related('professor'), id=vaga_id)

    dados = {}

    dados['vaga'] = vaga

    return render(request, 'project/view_vaga.html', dados)


@login_required
def create_vaga(request):
    context = {}
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    user = get_object_or_404(Professor, pk=request.user.id)
    form = JobForm(request.POST or None, initial={
                   "professor": user, "dataCadastro": date})

    if form.is_valid():
        print('passou')
        form.save()
        return redirect('index')

    context['form'] = form
    context['title'] = "Cadastrar vagas"

    return render(request, 'project/forms.html', context)


@login_required
def change_vaga(request, vaga_id):
    nome = request.user
    date = datetime.datetime.today().strftime('%Y-%m-%d')

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
        return redirect('index')

    context["form"] = form
    context["title"] = "Alterar vaga"

    return render(request, "project/forms.html", context)


@login_required
def search(request):
    # print('teste')
    vagas = vagasEmprego.objects.all().order_by('-dataCadastro')

    if 'search' in request.GET:
        search_name = request.GET['search']
        if search_name:
            vagas = vagas.filter(tituloVaga__icontains=search_name)

    dados = {
        'vagas': vagas
    }

    return render(request, 'project/search.html', dados)


@login_required
def delete_job(request, vaga_id):
    nome = request.user

    context = {}
    job = get_object_or_404(vagasEmprego, pk=vaga_id)
    context['title'] = 'deletar vaga'
    context['vaga'] = job

    if job.professor.user != nome:
        messages.error(request, "Você não pode realizar essa operação!")
        return redirect("index")

    if request.method == "POST":
        job.delete()
        return redirect('index')

    return render(request, 'project/delete.html', context)
