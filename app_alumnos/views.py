from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render, redirect 
from app_alumnos.models import Alumnos
import random
from app_alumnos.forms import CrearAlumnoForm, BuscarAlumnoForm, EditarAlumnoForm
from django.contrib.auth.decorators import login_required


#### PAGINA DE INICIO

def home(request):
    return render(request, 'app_alumnos/home.html', {})

def home_login(request):
    return render(request, 'app_alumnos/home_login.html', {})

#### BUSCAR UN ALUMNO

def alumno_buscar(request):
    
    formulario_buscar = BuscarAlumnoForm(request.GET)  

    if formulario_buscar.is_valid():
        
        nombre_a_buscar = formulario_buscar.cleaned_data.get('nombre')
        apellido_a_buscar = formulario_buscar.cleaned_data.get('apellido')
       
        resultado_alumno = Alumnos.objects.filter(
            nombre__icontains=nombre_a_buscar,
            apellido__icontains=apellido_a_buscar
        )
    else:
        resultado_alumno = []  

    # Renderizar la página con el formulario y los resultados
    return render(request, 'app_alumnos/alumno_buscar.html', {
        'db_alumnos': resultado_alumno,
        'formulario': formulario_buscar,
    })

#### VER UN ALUMNO

def alumno_ver(request, id_alumno):
    
    alumno = Alumnos.objects.get(id = id_alumno)
    
    return render(request, 'app_alumnos/alumno_ver.html', {'alumno': alumno})

# no quiero que cualquiera pueda crear/modificar/eliminar a un alumno. Se limita. 

#### CREACION DE UN ALUMNO NUEVO

@login_required
def alumno_nuevo(request):
     
    formulario = CrearAlumnoForm()
    
    if request.method == 'POST':
        formulario = CrearAlumnoForm(request.POST)   
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            alumno = Alumnos(nombre=data.get('nombre'), 
                           apellido =data.get('apellido'), 
                           anio_nacimiento=data.get('anio_nacimiento'), 
                            email = data.get('email'))
            alumno.save() 
            
            return redirect ('app_alumnos:alumno_buscar')

    return render(request, 'app_alumnos/alumno_nuevo.html', {'formulario':formulario}) #mi contexto ahora es el formulario


#### EDITAR ALUMNO

@login_required
def alumno_editar(request, id_alumno):
    
    alumno = Alumnos.objects.get(id = id_alumno)
    
    formulario = EditarAlumnoForm(initial = {
        'nombre': alumno.nombre, 
        'apellido': alumno.apellido,
        'anio_nacimiento': alumno.anio_nacimiento,
        'email':alumno.email
        })
   
    if request.method == 'POST':
        formulario = EditarAlumnoForm(request.POST)   
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            alumno.nombre = data.get('nombre')
            alumno.apellido = data.get('apellido')
            alumno.anio_nacimiento = data.get('anio_nacimiento')
            alumno.email = data.get('email')
            
        alumno.save()
        
        return redirect ('app_alumnos:alumno_buscar')
    
    return render(request, 'app_alumnos/alumno_editar.html', {'formulario':formulario,'alumno': alumno})


#### ELIMINAR ALUMNO

@login_required
def alumno_eliminar(request, id_alumno):
    
    alumno = Alumnos.objects.get(id = id_alumno)
    
    alumno.delete()
    
    return render(request, 'app_alumnos/alumno_eliminar.html', {'alumno': alumno})