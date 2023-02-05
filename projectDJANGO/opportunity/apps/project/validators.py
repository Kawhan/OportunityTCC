import jwt
from auth_django.models import User
from django.conf import settings

NOTA_MAXIMA = 10
NOTA_MINIMA = 0


class ValidaVagas:
    @staticmethod
    def hora_valida(data):
        return data['dataCadastro'] > data['dataFechamento']

    @staticmethod
    def valida_vagas(data):
        return data['numeroVagas'] < 0

    @staticmethod
    def valida_salario(data):
        return data['valorSalario'] <= 0

    @staticmethod
    def valida_horas_semana(data):
        return data['horasSemana'] <= 0

    validadores_vagas = {
        'hora_valida': lambda data: data if not ValidaVagas.hora_valida(data)
        else {"dataFechamento": "Precisa ser depois da data de cadastro"},
        'valida_vagas': lambda data: data if not ValidaVagas.valida_vagas(data)
        else {"numeroVagas": "As vagas preisam ser maior que 0"},
        'valida_salario': lambda data: data if not ValidaVagas.valida_salario(data)
        else {"valorSalario": "Valor salario não pode ser menor que 0"},
        'valida_horas_semanas': lambda data: data if not ValidaVagas.valida_horas_semana(data)
        else {"horasSemana": "O valor de horas semanas tem de ser maior que 0"},
    }


class ValidaAluno:
    @staticmethod
    def valida_CRA(data):
        return data['CRA'] < NOTA_MINIMA or data['CRA'] > NOTA_MAXIMA

    @staticmethod
    def valida_data(data):
        return data['dataEstimadaSaida'] < data['dataIngresso']

    valida_aluno = {
        'cra_valido': lambda data: data if not ValidaAluno.valida_CRA(data)
        else {"CRA": "Precisa ser maior que 0 e menor que 10"},
        'data_valida': lambda data: data if not ValidaAluno.valida_data(data)
        else {"dataEstimadaSaida": "A data de saida não pode ser antes da data de ingresso na faculdade"}
    }
