from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from apps.project.views import AlunosViewSet, InscricaoViewSet, ProfessorViewSet, vagasEmpregoViewSet, areaInteresseViewSet, professorVagasCadastradasViewSet, professorAreaInteresseViewSet, ListaIncricoesAlunoViewSet, ListaInscricoesVagaViewSet

router = routers.DefaultRouter()

router.register(r'alunos', AlunosViewSet, basename="Alunos")
router.register(r'inscricoes', InscricaoViewSet, basename="Inscricoes")
router.register(r'professor', ProfessorViewSet, basename="Professores")
router.register(r'vagas', vagasEmpregoViewSet, basename="Vagas")
router.register(r'areaInteresse', areaInteresseViewSet,
                basename="AreaInteresse")

urlpatterns = [
    path('admin', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('professor/<int:pk>/cadastros/',
         professorVagasCadastradasViewSet.as_view()),
    path('professor/<int:pk>/interesses/',
         professorAreaInteresseViewSet.as_view()),
    path('aluno/<int:pk>/inscricoes/', ListaIncricoesAlunoViewSet.as_view()),
    path('vaga/<int:pk>/inscricoes/', ListaInscricoesVagaViewSet.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
