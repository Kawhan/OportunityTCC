from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from apps.project.views import AlunosViewSet, InscricaoViewSet, ProfessorViewSet, vagasEmpregoViewSet, areaInteresseViewSet, professorVagasCadastradasViewSet, professorAreaInteresseViewSet, ListaIncricoesAlunoViewSet, ListaInscricoesVagaViewSet

router = routers.DefaultRouter()

router.register(r'alunos', AlunosViewSet, basename="Alunos")
router.register(r'inscricoes', InscricaoViewSet, basename="Inscricoes")
router.register(r'professor', ProfessorViewSet, basename="Professores")
router.register(r'vagas', vagasEmpregoViewSet, basename="Vagas")
router.register(r'areaInteresse', areaInteresseViewSet,
                basename="AreaInteresse")


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('professor/<int:pk>/cadastros/',
         professorVagasCadastradasViewSet.as_view()),
    path('professor/<int:pk>/interesses/',
         professorAreaInteresseViewSet.as_view()),
    path('aluno/<int:pk>/inscricoes/', ListaIncricoesAlunoViewSet.as_view()),
    path('vaga/<int:pk>/inscricoes/', ListaInscricoesVagaViewSet.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('auth_django.urls')),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path("accounts/",  include("django.contrib.auth.urls"))

]

admin.site.site_title = "Opportunity"
admin.site.site_header = "Opportunity admin site"
admin.site.index_title = "Opportunity Admin"
