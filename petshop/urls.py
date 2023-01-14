from django.contrib import admin
from django.urls import path, include
from base.views import *



urlpatterns = [
   
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('reserva/', include('reserva.urls', namespace='reserva')),
    path('admin/', admin.site.urls),
]
