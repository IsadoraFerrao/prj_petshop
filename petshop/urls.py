from django.contrib import admin
from django.urls import path, include
from base.views import *



urlpatterns = [
    path('base/', include('base.urls', namespace='base')),
    path('reserva/', include('reserva.urls', namespace='reserva')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls', namespace='api')),
]
