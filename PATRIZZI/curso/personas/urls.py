"""
URL configuration for personas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from personas.views import hola
from personas.views import inicio

from personas.views import obtener_fecha_actual

from personas.views import principal

from personas.views import personas_ingresar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ruta_saludo/', hola),
    path('inicio/', inicio),
    path('fecha_actual/',obtener_fecha_actual),
    path('',principal),
    path('personas_ingresar/',personas_ingresar),
    
]
#from personas.views import inicio1
#path('', inicio1),