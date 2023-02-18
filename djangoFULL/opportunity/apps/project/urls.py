from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('forms', create_vaga, name="form"),
    path('<int:vaga_id>/view-vaga', view_vaga, name="view_vaga"),
    path('<int:vaga_id>/change-vaga', change_vaga, name="change_vaga"),
    path('search', search, name="search"),
    path('<int:vaga_id>/delete-vaga', delete_job, name="delete_vaga"),
]
