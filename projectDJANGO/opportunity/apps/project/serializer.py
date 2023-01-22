from rest_framework import serializers
from project.models import Aluno, areaInteresse, Inscricao, Professor, vagasEmprego
from project.validators import *


class ProfessorSerializer(serializers.ModelSerializer):
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
        fields = '__all__'

    def validate(self, data):
        for k, v in ValidaAluno.valida_aluno.items():
            if v(data) != data:
                raise serializers.ValidationError(
                    v(data))

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
