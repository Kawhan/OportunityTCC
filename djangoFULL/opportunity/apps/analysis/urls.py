from django.urls import path

from .views import *

urlpatterns = [
    path('analises', analises, name="analises"),
    path('<int:vaga_id>/individual', indiviual_analysis, name="individual")
]
