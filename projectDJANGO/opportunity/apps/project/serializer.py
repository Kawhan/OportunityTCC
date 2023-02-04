import jwt
from auth_django.models import User
from django.conf import settings
from project.models import (Aluno, Inscricao, Professor, areaInteresse,
                            vagasEmprego)
from project.validators import *
from rest_framework import serializers


class ProfessorSerializer(serializers.ModelSerializer):
    """ Serializer para o professor """
    class Meta:
        model = Professor
        fields = '__all__'


class areaInteresseSerializer(serializers.ModelSerializer):
    professor_name = serializers.ReadOnlyField(
        source='professor_id.nomeProfessor')

    class Meta:
        model = areaInteresse
        fields = [
            'professor_id',
            'interesseProfessor',
            'professor_name'
        ]


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)


class vagasEmpregoSerializer(serializers.ModelSerializer):
    professor_name = serializers.ReadOnlyField(
        source='professor_id.nomeProfessor')

    class Meta:
        model = vagasEmprego
        fields = [
            'id',
            'numeroVagas',
            'nivel',
            'horasSemana',
            'valorSalario',
            'dataCadastro',
            'tipoVaga',
            'beneficios',
            'tituloVaga',
            'descricao',
            'dataFechamento',
            'professor_id',
            'professor_name'
        ]

    def validate(self, data):
        for k, v in ValidaVagas.validadores_vagas.items():
            if v(data) != data:
                raise serializers.ValidationError(
                    v(data))

        return data


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = (
            'matriculaAluno',
            'dataIngresso',
            'nomeAluno',
            'periodo',
            'CRA',
            'dataEstimadaSaida',
            'user',
        )

    def validate(self, data):
        for k, v in ValidaAluno.valida_aluno.items():
            if v(data) != data:
                raise serializers.ValidationError(
                    v(data))
        user = self.context['request'].user
        data['user'] = user
        return data


class InscricaoSerializer(serializers.ModelSerializer):
    nome_aluno = serializers.ReadOnlyField(source='IDAluno.nomeAluno')
    titulo_vaga = serializers.ReadOnlyField(source='IDVAGA.tituloVaga')

    class Meta:
        model = Inscricao
        fields = [
            'id',
            'IDAluno',
            'IDVAGA',
            'nome_aluno',
            'titulo_vaga'
        ]


class ListaCadastroVagasProfessorSerializer(serializers.ModelSerializer):
    nivel = serializers.SerializerMethodField()
    professor_name = serializers.ReadOnlyField(
        source='professor_id.nomeProfessor')

    class Meta:
        model = vagasEmprego
        fields = [
            'numeroVagas',
            'nivel',
            'horasSemana',
            'valorSalario',
            'dataCadastro',
            'tipoVaga',
            'beneficios',
            'tituloVaga',
            'descricao',
            'dataFechamento',
            'professor_id',
            'professor_name'
        ]

    def get_nivel(self, obj):
        return obj.get_nivel_display()


class ListaInteresseProfessorSerializer(serializers.ModelSerializer):
    professor_name = serializers.ReadOnlyField(
        source='professor_id.nomeProfessor')

    class Meta:
        model = areaInteresse
        fields = [
            'professor_id',
            'interesseProfessor',
            'professor_name'
        ]


class ListaIncricoesAlunoSerializer(serializers.ModelSerializer):
    nome_aluno = serializers.ReadOnlyField(source='IDAluno.nomeAluno')
    titulo_vaga = serializers.ReadOnlyField(source='IDVAGA.tituloVaga')

    class Meta:
        model = Inscricao
        fields = [
            'id',
            'IDAluno',
            'IDVAGA',
            'nome_aluno',
            'titulo_vaga'
        ]


class ListaIncricoesVagaSerializer(serializers.ModelSerializer):
    nome_aluno = serializers.ReadOnlyField(source='IDAluno.nomeAluno')
    titulo_vaga = serializers.ReadOnlyField(source='IDVAGA.tituloVaga')

    class Meta:
        model = Inscricao
        fields = [
            'id',
            'IDAluno',
            'IDVAGA',
            'nome_aluno',
            'titulo_vaga'
        ]
