import datetime

from accounts.models import User, UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from project.forms import JobForm
from project.models import Professor, vagasEmprego


@login_required
def grafics(request, vaga_id):
    count_alunos_SI = 0
    count_alunos_LCC = 0

    count_num_inscritos = vagasEmprego.objects.filter(
        id=vaga_id).values('aluno').count()

    alunos = vagasEmprego.objects.filter(
        id=vaga_id).values('aluno')

    for aluno in alunos:
        info = UserProfile.objects.filter(id=aluno['aluno']).values('curso')
        if info[0]['curso'] == 'SI':
            count_alunos_SI += 1
        elif info[0]['curso'] == 'LCC':
            count_alunos_LCC += 1

    print(
        f'Quantidade de alunos de SI {count_alunos_SI} | Quantidade de alunos de LCC {count_alunos_LCC}')

    return redirect('index')

    pass
