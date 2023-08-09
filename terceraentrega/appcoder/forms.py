from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CursoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la comisión", max_length=50, required=True)
    comision = forms.IntegerField(label="Comision", min_value=1000, max_value=9999, required=True)
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )
    turno = forms.ChoiceField(label="Turno elegido", choices=TURNOS, required=True)
    
class ProfesorForm(forms.Form):
    nombre = forms.CharField(label="Nombre del profesor", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del profesor", max_length=50, required=True)
    email = forms.EmailField(label="Email del profesor", required=False)
    profesion = forms.CharField(label="Profesión del profesor", max_length=50, required=True)
    
class EstudianteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del alumno", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del profesor", max_length=50, required=True)
    email = forms.EmailField(label="Email del alumno", required=False)
    
class EntregableForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la comisión", max_length=50, required=True)
    entregado = forms.BooleanField(label="¿El trabajo ha sido entregado?", required=True)
    fechaEntrega = forms.DateField(label="Fecha de entrega")
    
class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombres", max_length=50, required=False)
    last_name = forms.CharField(label="Apellidos", max_length=50, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)