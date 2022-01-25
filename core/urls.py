from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path(f'veiculos/<str:categoria>', veiculos, name='veiculos'),
    path(f'veiculo/<int:pk>', perfil_veiculo, name='perfil_veiculo'),
]