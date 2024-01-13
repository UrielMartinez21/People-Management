from django.http import HttpResponse
from django.shortcuts import render

from usuarios.models import Domicilio, Usuario

# Create your views here.
def bienvenido(request):
    # Usuarios
    no_usuarios = Usuario.objects.count()
    usuarios = Usuario.objects.all().order_by('id')

    # Direcciones
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.all().order_by('id')

    # Objeto
    objeto = {
        'no_usuarios':no_usuarios, 
        'usuarios':usuarios,
        'no_domicilios': no_domicilios,
        'domicilios':domicilios,
    }
    return render(request, 'bienvenido.html', objeto)


def despedirse(request):
    return HttpResponse('Adios mundo desde django')