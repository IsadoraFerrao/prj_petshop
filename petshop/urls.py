from django.contrib import admin
from django.urls import path
from base.views import *

app_name = 'base'

urlpatterns = [
    path('contato/', contato, name='contato'),
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
]
