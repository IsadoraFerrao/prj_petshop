from django.urls import path
from rest_api.views import hello_world,reserva_de_banho

app_name = 'rest_api'

urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api'),
    path('reserva_de_banho/', reserva_de_banho, name='reserva_de_banho'),
]