from datetime import datetime

from accounts.models import User, UserProfile
from django.forms import ModelForm, ValidationError


def nome_invalid(nome, user, nome_campo, lista_erros):
    """ Verifica se o nome é valido """
    if nome == None:
        lista_erros[nome_campo] = "Nome vazio!"
        return

    user_provider = UserProfile.objects.select_related(
        'user').filter(nome=nome).values_list('user', flat=True).order_by('id')

    if UserProfile.objects.filter(nome=nome).exists() and user_provider[0] != user.id:
        lista_erros[nome_campo] = "Nome já cadastrado em outro usuário!"
        return

    if any(char.isdigit() for char in nome):
        lista_erros[nome_campo] = "Não inclua números no campo nome!"
        return


def matricula_invalid(matricula, user, nome_campo, lista_erros):
    """ Verifica se a matricula é valida """
    if matricula == None:
        lista_erros[nome_campo] = "Campo Matricula Vazio!"
        return

    user_provider = UserProfile.objects.select_related(
        'user').filter(matricula=matricula).values_list('user', flat=True).order_by('id')

    if UserProfile.objects.filter(matricula=matricula).exists() and user_provider[0] != user.id:
        lista_erros[nome_campo] = "Está matricula já existe!"
        return

    if len(matricula) != 11:
        lista_erros[nome_campo] = "Está matricula tem um número incorreto de caracteres"
        return

    if (not matricula.isnumeric()):
        lista_erros[nome_campo] = "A matricula não pode conter letras apenas números"
        return


def email_not_dcx(email, nome_campo, lista_de_erros):
    """ Verifica se o e-mail é valido """
    domain = email.split('@')[1]

    if domain != 'dcx.ufpb.br':
        lista_de_erros[nome_campo] = "Email não é dcx"
        return


def curso_invalid(curso, nome_campo, lista_de_erros):
    """ Verifica se o curso é valido """
    if curso == None:
        lista_de_erros[nome_campo] = "Curso não pode ficar vazio"
        return

    if curso != 'SI' and curso != 'LCC':
        lista_de_erros[nome_campo] = "Curso invalido"
        return


def period_invalid(periodo, nome_campo, lista_de_erros):
    """ Verifica se o periodo é válido """
    if periodo == None:
        lista_de_erros[nome_campo] = "Periodo não pode ficar vazio"
        return
