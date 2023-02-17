from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from project.models import vagasEmprego


# View of vagas
def index(request):
    vagas = vagasEmprego.objects.all()

    paginator = Paginator(vagas, 3)
    page = request.GET.get('page')
    vagas_per_page = paginator.get_page(page)

    dados = {}

    dados['vagas'] = vagas_per_page
    dados['title'] = "Home"

    return render(request, 'project/index.html', dados)


def view_vaga(request, vaga_id):
    vaga = get_object_or_404(
        vagasEmprego.objects.select_related('professor_id'), id=vaga_id)

    dados = {}

    dados['vaga'] = vaga

    return render(request, 'project/view_vaga.html', dados)
