from django.contrib import admin
from django.urls import path
from base.views import inicio

urlpatterns = [
    path('', inicio),
    path('admin/', admin.site.urls),
]
