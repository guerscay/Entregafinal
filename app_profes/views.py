from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from app_profes.models import Profes
from django.urls import reverse_lazy


# Visualizacion de la database de profesores de COOLates
class VerProfes(ListView):
    model = Profes
    template_name = "app_profes/profes_buscar.html"
    
    # para no usar el object_list que viene by default en el template uso
    context_object_name ='db_profes'
    
# Creación de un nuevo profesor
class CrearProfe(CreateView):
    model = Profes  # eso viene del model, entonces se trae igual
    template_name = "app_profes/profe_nuevo.html"
    fields = ['nombre', 'apellido', 'certificacion', 'horas_semana', 'fecha_ingreso']   # los campos de mi formulario
    success_url = reverse_lazy('app_profes:profe_nuevo')
    

