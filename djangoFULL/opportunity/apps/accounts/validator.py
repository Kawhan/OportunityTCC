
def nome_invalid(nome, nome_campo, lista_erros):
    """ Verifica se o nome é valido """

    if any(char.isdigit() for char in nome):
        lista_erros[nome_campo] = "Não inclua números neste campo!"
