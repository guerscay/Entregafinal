from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from app_acceso.forms import Registro_Usuario, EditarPerfil
from django.contrib.auth.decorators import login_required 


# LOGIN DE USUARIOS
def acceso_login(request):
    
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('app_alumnos:home_login')
    
    
    return render(request, 'app_acceso/acceso_login.html', {'form' : form} )


# REGISTRO DE USUARIOS
def acceso_registro(request):
    
    formulario = Registro_Usuario()
    
    if request.method == 'POST':
        formulario = Registro_Usuario(request.POST)
        if formulario.is_valid:
            formulario.save()
        
        return redirect('app_acceso:acceso_login')
               
    return render (request, 'app_acceso/acceso_registro.html', {'form':formulario})

# PERFIL DEL USUARIO
@login_required
def acceso_perfil (request):
    return render(request, 'app_acceso/acceso_perfil.html', {})

@login_required
def acceso_perfil_editar(request):
    formulario = EditarPerfil(instance = request.user)
    
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST,instance = request.user )
        if formulario.is_valid:
            formulario.save()
        
        return redirect('app_acceso:acceso_perfil')
               
    return render (request, 'app_acceso/acceso_perfil_editar.html', {'form': formulario})