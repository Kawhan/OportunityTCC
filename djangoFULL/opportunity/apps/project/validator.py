def numero_vagas_invalido(vagas, nome_campo, lista_erros):
    """ Verifica se o número de vagas é valido """
    if vagas is None:
        return

    if int(vagas) <= 0:
        lista_erros[nome_campo] = "Número de vagas invalido! Valor deve ser maior que 0"
        return


def horas_semana_invalida(horas_semana, nome_campo, lista_erros):
    """ Verifica se o número de horas semana é invalido """
    if horas_semana is None:
        return

    if int(horas_semana) <= 0:
        lista_erros[nome_campo] = "Número de horas semana invalido! Valor deve ser maior que 0"
        return


def valor_salario_invalido(valor_salario, nome_campo, lista_erros):
    """ Verifica se o valor do salario ou bolsa é valido """

    if valor_salario is None:
        return

    if valor_salario <= 0:
        lista_erros[nome_campo] = "Campo de valor salario/bolsa invalido! Valor deve ser maior que 0"
        return


def date_invalid(data_cadastro, data_fechamento, nome_campo, lista_erros):
    """ Verifica se as datas estão em um estado correto"""
    if data_cadastro == None or data_fechamento == None:
        return

    if data_cadastro > data_fechamento:
        lista_erros[nome_campo] = "Data de entrada não pode ser maior que data saida"
        return
