from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from project.serializer import AlunoSerializer, areaInteresseSerializer, ProfessorSerializer, vagasEmpregoSerializer, InscricaoSerializer, ListaCadastroVagasProfessorSerializer, ListaInteresseProfessorSerializer, ListaIncricoesAlunoSerializer, ListaIncricoesVagaSerializer
from project.models import Aluno, Inscricao, areaInteresse, Professor, vagasEmprego


class ProfessorViewSet(viewsets.ModelViewSet):
    """ Exibindo tofdos os professores """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class areaInteresseViewSet(viewsets.ModelViewSet):
    """ Exibindo as áreas de interesse de cada professor """
    queryset = areaInteresse.objects.select_related("professor_id").all()
    serializer_class = areaInteresseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class vagasEmpregoViewSet(viewsets.ModelViewSet):
    """ Exibindo as vagas de emprego cadastradas """
    queryset = vagasEmprego.objects.select_related('professor_id').all()
    serializer_class = vagasEmpregoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AlunosViewSet(viewsets.ModelViewSet):
    """  Exibindo os alunos cadastrados """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class InscricaoViewSet(viewsets.ModelViewSet):
    """ Exibindo as inscricoes de cada pessoa """
    queryset = Inscricao.objects.select_related(
        'IDAluno').select_related('IDVAGA').all()
    serializer_class = InscricaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class professorVagasCadastradasViewSet(generics.ListAPIView):
    """ Exibindo as vagas cadastradas de um professor especifico """

    def get_queryset(self):
        queryset = vagasEmprego.objects.filter(
            professor_id=self.kwargs['pk']).select_related('professor_id').all()
        return queryset

    serializer_class = ListaCadastroVagasProfessorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class professorAreaInteresseViewSet(generics.ListAPIView):
    """ Exibindo os interesses de um professor especifico """

    def get_queryset(self):
        queryset = areaInteresse.objects.filter(
            professor_id=self.kwargs['pk']).select_related('professor_id').all()
        return queryset

    serializer_class = ListaInteresseProfessorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaIncricoesAlunoViewSet(generics.ListAPIView):
    """ Exibindo todas as inscricoes de um determinado aluno"""

    def get_queryset(self):
        queryset = Inscricao.objects.filter(IDAluno=self.kwargs['pk']).select_related(
            'IDAluno').select_related('IDVAGA').all()
        return queryset

    serializer_class = ListaIncricoesAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaInscricoesVagaViewSet(generics.ListAPIView):
    """ Exibindo todas as pessoas inscritas em uma vaga """

    def get_queryset(self):
        queryset = Inscricao.objects.filter(IDVAGA=self.kwargs['pk']).select_related(
            'IDAluno').select_related('IDVAGA').all()
        return queryset

    serializer_class = ListaIncricoesVagaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
