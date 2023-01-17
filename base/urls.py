from django.urls import path
from base.views import *

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
]