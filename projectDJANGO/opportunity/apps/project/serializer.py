from rest_framework import serializers
from project.models import Aluno, areaInteresse, Inscricao, Professor, vagasEmprego

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class areaInteresseSerializer(serializers.ModelSerializer):
    professor_name  = serializers.ReadOnlyField(source='professor_id.nomeProfessor')
    
    class Meta:
        model = areaInteresse
        fields = [
            'professor_id',
            'interesseProfessor',
            'professor_name'
        ]

class vagasEmpregoSerializer(serializers.ModelSerializer):
    nivel = serializers.SerializerMethodField()
    professor_name  = serializers.ReadOnlyField(source='professor_id.nomeProfessor')
    
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

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        
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
        