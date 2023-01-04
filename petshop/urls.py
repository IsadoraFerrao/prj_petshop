from django.contrib import admin
from django.urls import path
from base.views import *

app_name = 'base'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('contato/', contato, name='contato'),
    path('admin/', admin.site.urls),
]
