from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.project.views import AlunosViewSet, InscricaoViewSet, ProfessorViewSet, vagasEmpregoViewSet, areaInteresseViewSet

router = routers.DefaultRouter()

router.register('alunos', AlunosViewSet, basename="Alunos")
router.register('inscricoes', InscricaoViewSet, basename="Inscricoes")
router.register('professor', ProfessorViewSet, basename="Professores")
router.register('vagas', vagasEmpregoViewSet, basename="Vagas")
router.register('areaInteresse', areaInteresseViewSet, basename="AreaInteresse")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
