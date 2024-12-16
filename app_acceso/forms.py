from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from app_acceso.models import AccesoInfoUsuario



class Registro_Usuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(max_length=8, label = 'Clave', widget = forms.PasswordInput)
    password2 = forms.CharField(max_length=8, label = 'Repetir Clave', widget = forms.PasswordInput)
    first_name = forms.CharField(max_length=40, label = 'Nombre', required = False)
    last_name = forms.CharField(max_length=40, label = 'Apellido', required = False)
       
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {
            key : ''
            for key in fields}
        
        
   
class EditarPerfil(UserChangeForm):
    email = forms.CharField(max_length=40, label='Email', required=False)
    password = None
    first_name = forms.CharField(max_length=40, label='Nombre', required=False)
    last_name = forms.CharField(max_length=40, label='Apellido', required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {
            key: ''
            for key in fields
        }

class EditarAvatar(forms.ModelForm):
    class Meta:
        model = AccesoInfoUsuario
        fields = ['avatar']
