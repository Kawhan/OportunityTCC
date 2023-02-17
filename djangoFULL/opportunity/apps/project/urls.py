from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('<int:vaga_id>/view-vaga', view_vaga, name="view_vaga")
]
