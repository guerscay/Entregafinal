from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render 
from app_alumnos.models import Alumnos
import random
from app_alumnos.forms import CrearAlumnoForm, BuscarAlumnoForm


#### PAGINA DE INICIO

def home(request):
    return render(request, 'app_alumnos/home.html', {})

#### CREACION DE UN ALUMNO NUEVO

def alumno_nuevo(request):
     
    formulario = CrearAlumnoForm()
    
    if request.method == 'POST':
        formulario = CrearAlumnoForm(request.POST)   
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            auto = Alumnos(nombre=data.get('nombre'), 
                           apellido =data.get('apellido'), 
                           anio_nacimiento=data.get('anio_nacimiento'), 
                            email = data.get('email'))
            auto.save() 
            
            return render(request, 'app_alumnos/home.html',{})

    return render(request, 'app_alumnos/alumno_nuevo.html', {'formulario':formulario}) #mi contexto ahora es el formulario


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
