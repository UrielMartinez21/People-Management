"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from usuarios.views import detalle_domicilio, detalleUsuario, editar_domicilio, editar_usuario, eliminar_domicilio, eliminar_usuario, nuevo_domicilio, nuevoUsuario
from webapp.views import bienvenido, despedirse

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',                                             # URL que se va a procesar           
        bienvenido,                                     # Funcion que se va a ejecutar                   
        name='index'                                    # Nombre con el que se puede referenciar a esta url
    ),

    path('despedirse/', despedirse),
    # --> Usuarios
    path('nuevo_usuario/', nuevoUsuario),
    path('detalle_usuario/<int:id>', detalleUsuario),
    path('editar_usuario/<int:id>', editar_usuario),
    path('eliminar_usuario/<int:id>', eliminar_usuario),
    # --> Domicilios
    path('detalle_domicilio/<int:id>', detalle_domicilio),
    path('nuevo_domicilio/', nuevo_domicilio),
    path('editar_domicilio/<int:id>', editar_domicilio),
    path('eliminar_domicilio/<int:id>', eliminar_domicilio),
]
