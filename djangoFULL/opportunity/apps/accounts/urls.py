from django.urls import path

from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('profile/', update_profile, name='profile'),
    path('activate/<uidb64>/<token>', activate, name='activate')
]
