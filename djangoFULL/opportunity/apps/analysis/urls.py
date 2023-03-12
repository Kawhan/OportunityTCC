from django.urls import path

from .views import *

urlpatterns = [
    path('analises', analises, name="analises")
]
