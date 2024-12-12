from django import forms
from app_alumnos.models import Alumnos

class FormularioBaseForm(forms.Form):
    nombre = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}))
    apellido = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Tu apellido'}))
    anio_nacimiento = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '2000'}))
    email = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'ejemplo@email.com'}))

class CrearAlumnoForm(FormularioBaseForm):
    ...
    
class EditarAlumnoForm(FormularioBaseForm):
    ...

class BuscarAlumnoForm(forms.Form):
    nombre = forms.CharField(required=False, label="Nombre", widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(required=False, label="Apellido", widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))

