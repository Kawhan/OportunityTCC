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


def idade_invalid(idade, nome_campo, lista_de_erros):
    if idade == None:
        lista_de_erros[nome_campo] = "Campo de idade vazio!"
        return

    if idade <= 0:
        lista_de_erros[nome_campo] = "Campo de idade invalido!"
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


def periodo_invalid(periodo, nome_campo, lista_erros):
    """ Verificar se o periodo é valido """
    range_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    if (periodo not in range_numbers):
        lista_erros[nome_campo] = "O periodo mencionado não é valido"


def cra_invalid(cra, nome_campo, lista_erros):
    """ Verificando se o CRA é valido """
    if cra == None:
        lista_erros[nome_campo] = "Campo CRA vazio!"
        return

    if cra < 0.0 or cra > 10.0:
        lista_erros[nome_campo] = "CRA invalido, por favor coloque um valor entre 0.0 e 10.0"
        return


def date_in_invalid(data_ingresso, data_saida, nome_campo, lista_erros):
    """ Verifica data de entrada é maior que a data de saida"""
    if data_ingresso == None or data_saida == None:
        lista_erros[nome_campo] = "Data de entrada ou Data de saida vazios"
        return

    if data_ingresso > data_saida:
        lista_erros[nome_campo] = "Data de entrada não pode ser maior que data saida"
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


def nota_introducao_invalid(nota_introducao, nome_campo, lista_de_erros):
    """ Verifica se a nota de introdução a programação é valida """
    if nota_introducao == None:
        lista_de_erros[nome_campo] = "Campo de nota de introdução a programação não pode ficar vazio"
        return

    if nota_introducao > 10 or nota_introducao < 0:
        lista_de_erros[nome_campo] = "Nota de introdução a programação tem de ser maior que 0 e menor ou igual a 10"
        return


def nota_POO_invalid(nota_POO, nome_campo, lista_de_erros):
    """ Verifica se a nota de POO é valida """
    if nota_POO != None:
        if nota_POO < 0 or nota_POO > 10:
            lista_de_erros[nome_campo] = "Nota de POO tem de ser maior que 0 e menor ou igual a 10"
            return


def nota_linguagem_invalid(nota_linguagem, nome_campo, lista_de_erros):
    """ Verifica se a nota de linguagem de programação é valida """
    if nota_linguagem != None:
        if nota_linguagem < 0 or nota_linguagem > 10:
            lista_de_erros[nome_campo] = "Nota de linguagem tem de ser maior que 0 e menor ou igual a 10"
            return


def nota_estrutura_invalid(nota_estrutura, nome_campo, lista_de_erros):
    """ Verifica se a noota de estrutura é valida """
    if nota_estrutura != None:
        if nota_estrutura < 0 or nota_estrutura > 10:
            lista_de_erros[nome_campo] = "Nota de estrutura de dados tem de ser maior que 0 e menor ou igual a 10"
            return


def disposicao_invalid(disposicao, nome_campo, lista_de_erros):
    """ Verifica se as horas de disposicao são validas """
    if disposicao == None:
        lista_de_erros[nome_campo] = "Campo de disposição não pode ficar vazio"
        return

    if disposicao != 'S' and disposicao != 'N':
        lista_de_erros[nome_campo] = "Campo de disposição com valor invalido"
        return


def numero_disciplinas_invalid(numero_disciplinas, nome_campo, lista_de_erros):
    """ Verifica se o número de disciplinas é valido """
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    if (numero_disciplinas not in numeros):
        lista_de_erros[nome_campo] = "O número de disciplinas mencionado não é valido"
