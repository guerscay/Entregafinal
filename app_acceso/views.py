from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from app_acceso.forms import Registro_Usuario, EditarPerfil, EditarAvatar
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from app_acceso.models import AccesoInfoUsuario

def acceso_about (request):
    return render(request, 'app_acceso/acceso_about.html', {} )

# LOGIN DE USUARIOS
def acceso_login(request):
    
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.get_user()
            
            login(request, usuario)
            
            AccesoInfoUsuario.objects.get_or_create(user = usuario)
            
            return redirect ('app_alumnos:home_login')
    
    
    return render(request, 'app_acceso/acceso_login.html', {'form' : form} )


# REGISTRO DE USUARIOS
def acceso_registro(request):
    
    formulario = Registro_Usuario()
    
    if request.method == 'POST':
        formulario = Registro_Usuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('app_acceso:acceso_login')
        
        else:
            print(formulario.errors)  
    return render(request, 'app_acceso/acceso_registro.html', {'form': formulario})


# PERFIL DEL USUARIO
@login_required
def acceso_perfil (request):
    return render(request, 'app_acceso/acceso_perfil.html', {})

@login_required
def acceso_perfil_editar(request):
    user = request.user
    info_usuario = user.accesoinfousuario  # Acceso al modelo relacionado
    
    # Formularios para User y AccesoInfoUsuario
    formulario_user = EditarPerfil(instance=user)
    formulario_avatar = EditarAvatar(instance=info_usuario)
    
    if request.method == 'POST':
        formulario_user = EditarPerfil(request.POST, instance=user)
        formulario_avatar = EditarAvatar(request.POST, request.FILES, instance=info_usuario)
        
        if formulario_user.is_valid() and formulario_avatar.is_valid():
            formulario_user.save()
            formulario_avatar.save()
            return redirect('app_acceso:acceso_perfil')
    
    return render(request, 'app_acceso/acceso_perfil_editar.html', {
        'form_user': formulario_user,
        'form_avatar': formulario_avatar,
    })



# se hace el cambio de password por clase basada en vista
class AccesoPassword(LoginRequiredMixin,PasswordChangeView):
    template_name = 'app_acceso/acceso_password.html'
    success_url = reverse_lazy('app_acceso:acceso_login')