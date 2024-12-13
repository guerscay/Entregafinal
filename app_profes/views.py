from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from app_profes.models import Profes
from django.urls import reverse_lazy


# Visualizacion de la database de profesores de COOLates
class ListaProfes(ListView):
    model = Profes
    template_name = "app_profes/profes_buscar.html"
    
    # para no usar el object_list que viene by default en el template uso
    context_object_name ='db_profes'
    
# Creación de un nuevo profesor
class CrearProfe(CreateView):
    model = Profes  # eso viene del model, entonces se trae igual
    template_name = "app_profes/profe_nuevo.html"
    fields = ['nombre', 'apellido', 'certificacion', 'horas_semana', 'fecha_ingreso']   # los campos de mi formulario
    success_url = reverse_lazy('app_profes:profes_buscar')
    
# Info de profes (Ver)
class InfoProfe(DetailView):
    model = Profes
    template_name = "app_profes/profe_info.html"
    # context_object_name = 'profe' no es necesario poner esto porque internamente 
    # django genera el contect_object_name como el nombre del modelo pero en minuscula
  
# Modificar profes (Editar)
class UpdateProfe(UpdateView):
    model = Profes
    template_name = "app_profes/profe_update.html"
    fields = ['nombre', 'apellido', 'certificacion', 'horas_semana', 'fecha_ingreso']
    success_url = reverse_lazy('app_profes:profes_buscar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar el objeto profe al contexto
        context['profe'] = self.get_object()
        return context

# Borrar profes (Delete)
class BorrarProfe(DeleteView):
    model = Profes
    template_name = "app_profes/profe_borrar.html"
    success_url = reverse_lazy('app_profes:profes_buscar')
