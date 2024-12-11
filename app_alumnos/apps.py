from django.apps import AppConfig
from django import forms


class AppAlumnosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_alumnos'




# class CrearAuto(forms.Form):
#     marca = forms.CharField(max_length=20)
#     modelo = forms.CharField(max_length=20)
#     anio = forms.IntegerField()
    
# class BuscarAuto(forms.Form):
#     marca = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Ford, Fiat, Chevrolet...'}))
#     modelo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Uno, K, 206...'}))
    