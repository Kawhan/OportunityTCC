from django.urls import path

from .views import *

urlpatterns = [
    path('<int:vaga_id>/grafico-vaga', grafics, name="graficos")
]
