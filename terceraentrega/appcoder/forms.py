from django import forms

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
    
class EstudianteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del alumno", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del profesor", max_length=50, required=True)
    email = forms.EmailField(label="Email del alumno", required=False)
    
class EntregableForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la comisión", max_length=50, required=True)
    entregado = forms.BooleanField(label="¿El trabajo ha sido entregado?", required=True)
    fechaEntrega = forms.DateField(label="Fecha de entrega")