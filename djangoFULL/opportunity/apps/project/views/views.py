from django.shortcuts import render
from project.models import vagasEmprego


# Create your views here.
def index(request):
    vagas = vagasEmprego.objects.all()

    dados = {}

    dados['vagas'] = vagas

    return render(request, 'project/index.html', dados)
