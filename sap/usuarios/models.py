from django.db import models

# Create your models here.

class Domicilio(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    localidad = models.CharField(max_length=50)

    def __str__(self):
        return f"Domicilio: {self.id} {self.calle} {self.numero} {self.localidad}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Persona: {self.id} {self.nombre} {self.apellido} {self.email}"