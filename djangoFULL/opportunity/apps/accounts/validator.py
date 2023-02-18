
def nome_invalid(nome, nome_campo, lista_erros):
    """ Verifica se o nome é valido """

    if any(char.isdigit() for char in nome):
        lista_erros[nome_campo] = "Não inclua números neste campo!"


def matricula_invalid(matricula, nome_campo, lista_erros):
    """ Verifica se a matricula é valida """
    if (not matricula.isnumeric()):
        lista_erros[nome_campo] = "A matricula não pode conter letras apenas números"


def periodo_invalid(periodo, nome_campo, lista_erros):
    """ Verificar se o periodo é valido """
    range_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    if (periodo not in range_numbers):
        lista_erros[nome_campo] = "O periodo mencionado não é valido"


def cra_invalid(cra, nome_campo, lista_erros):
    """ Verificando se o CRA é valido """

    if cra < 0.0 or cra > 10.0:
        lista_erros[nome_campo] = "CRA invalido, por favor coloque um valor entre 0.0 e 10.0"


def date_in_invalid(data_ingresso, data_saida, nome_campo, lista_erros):
    """ Verifica data de entrada é maior que a data de saida"""
    if data_ingresso > data_saida:
        lista_erros[nome_campo] = "Data de entrada não pode ser maior que data saida"