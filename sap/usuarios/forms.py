from django.forms import EmailInput, ModelForm, TextInput

from usuarios.models import Domicilio, Usuario


class UsuarioForm(ModelForm):
    class Meta:                                         # Metaclase      
        model = Usuario                                 # Modelo que se va a utilizar
        fields = '__all__'                              # Campos que se van a mostrar         
        widgets = {                                     # Widgets para los campos
            'email': EmailInput(attrs={'type':'email'}) # Campo email con widget de email
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'numero': TextInput(attrs={'type':'number'})
        }