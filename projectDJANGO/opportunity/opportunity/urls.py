from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.project.views import AlunosViewSet, InscricaoViewSet, ProfessorViewSet, vagasEmpregoViewSet, areaInteresseViewSet, professorVagasCadastradasViewSet, professorAreaInteresseViewSet, ListaIncricoesAlunoViewSet, ListaInscricoesVagaViewSet

router = routers.DefaultRouter()

router.register('alunos', AlunosViewSet, basename="Alunos")
router.register('inscricoes', InscricaoViewSet, basename="Inscricoes")
router.register('professor', ProfessorViewSet, basename="Professores")
router.register('vagas', vagasEmpregoViewSet, basename="Vagas")
router.register('areaInteresse', areaInteresseViewSet, basename="AreaInteresse")

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include(router.urls)),
     path('professor/<int:pk>/cadastros/', professorVagasCadastradasViewSet.as_view()),
     path('professor/<int:pk>/interesses/', professorAreaInteresseViewSet.as_view()),
     path('aluno/<int:pk>/inscricoes/', ListaIncricoesAlunoViewSet.as_view()),
     path('vaga/<int:pk>/inscricoes/', ListaInscricoesVagaViewSet.as_view())
]
