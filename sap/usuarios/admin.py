from django.contrib import admin

from usuarios.models import Domicilio, Usuario

# Register your models here.

# Esto para que se vea en el admin de django
admin.site.register(Usuario)
admin.site.register(Domicilio)