from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from usuarios.forms import DomicilioForm, UsuarioForm
from usuarios.models import Domicilio, Usuario

# Create your views here.


def detalleUsuario(request, id):
    """
    Muestra el detalle de un usuario en particular o un error 404
    """

    usuario = get_object_or_404(Usuario, pk=id)
    return render(request, 'usuarios/detalle.html', {'usuario':usuario})


def nuevoUsuario(request):
    """
    Crea un nuevo usuario si es que se hace un post
    o muestra la forma para crear un usuario
    """

    # --> Si es post se crea el usuario
    if request.method == 'POST':
        # Llenamos la forma con los datos guardados en post
        formaUsuario = UsuarioForm(request.POST)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('index')
    # --> Si no es post se crea la forma
    else:
        formaUsuario = UsuarioForm()
    # --> Renderiza la forma
    return render(request, 'usuarios/nuevo.html', {'formaUsuario':formaUsuario})


def editar_usuario(request, id):
    """
    Edita un usuario si es que se hace un post
    o muestra la forma para editar un usuario
    """

    # --> Obtenemos el usuario
    usuario = get_object_or_404(Usuario, pk=id)
    # --> Si es post se edita el usuario
    if request.method == 'POST':
        # Llenamos la forma con los datos guardados en post
        formaUsuario = UsuarioForm(request.POST, instance=usuario)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('index')
    # --> Si no es post se crea la forma
    else:
        # Creamos la forma con los datos del usuario
        formaUsuario = UsuarioForm(instance=usuario)
    # --> Renderiza la forma
    return render(request, 'usuarios/editar.html', {'formaUsuario':formaUsuario})


def eliminar_usuario(request, id):
    """
    Elimina un usuario si es que se hace un post
    o muestra la forma para eliminar un usuario
    """
    usuario = get_object_or_404(Usuario, pk=id)
    if usuario:
        usuario.delete()
        return redirect('index')
    
# -----------------| Domicilios |-----------------
def detalle_domicilio(request, id):
    """
    Muestra el detalle de un domilicio en particular o un error 404
    """

    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalle.html', {'domicilio':domicilio})


def nuevo_domicilio(request):
    """
    Crea un nuevo domicilio si es que se hace un post
    o muestra la forma para crear un usuario
    """

    # --> Si es post se crea el usuario
    if request.method == 'POST':
        # Llenamos la forma con los datos guardados en post
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    # --> Si no es post se crea la forma
    else:
        formaDomicilio = DomicilioForm()
    # --> Renderiza la forma
    return render(request, 'domicilios/nuevo.html', {'formaDomicilio':formaDomicilio})


def editar_domicilio(request, id):
    """
    Edita un domicilio si es que se hace un post
    o muestra la forma para editar un usuario
    """

    # --> Obtenemos el usuario
    domicilio = get_object_or_404(Domicilio, pk=id)

    # --> Si es post se edita el usuario
    if request.method == 'POST':
        # Llenamos la forma con los datos guardados en post
        formaDomicilio = DomicilioForm(request.POST, instance= domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    # --> Si no es post se crea la forma
    else:
        # Creamos la forma con los datos del usuario
        formaDomicilio = DomicilioForm(instance= domicilio)
    # --> Renderiza la forma
    return render(request, 'domicilios/editar.html', {'formaDomicilio':formaDomicilio})


def eliminar_domicilio(request, id):
    """
    Elimina un domicilio si es que se hace un post
    o muestra la forma para eliminar un usuario
    """
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
        return redirect('index')
