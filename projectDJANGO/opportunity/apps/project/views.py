from rest_framework import viewsets


from project.serializer import AlunoSerializer, areaInteresseSerializer, ProfessorSerializer, vagasEmpregoSerializer, InscricaoSerializer 
from project.models import Aluno, Inscricao, areaInteresse, Professor, vagasEmprego



class ProfessorViewSet(viewsets.ModelViewSet):
    """ Exibindo tofdos os professores """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    

class areaInteresseViewSet(viewsets.ModelViewSet):
    """ Exibindo as áreas de interesse de cada professor """
    queryset = areaInteresse.objects.select_related("professor_id").all()
    serializer_class = areaInteresseSerializer

class vagasEmpregoViewSet(viewsets.ModelViewSet):
    """ Exibindo as vagas de emprego cadastradas """
    queryset = vagasEmprego.objects.select_related('professor_id').all()
    serializer_class = vagasEmpregoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """  Exibindo os alunos cadastrados """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    """ Exibindo as inscricoes de cada pessoa """
    queryset = Inscricao.objects.select_related('IDAluno').select_related('IDVAGA').all()
    serializer_class = InscricaoSerializer
    