from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from app_profes.models import Profes
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Visualizacion de la database de profesores de COOLates
class ListaProfes(ListView):
    model = Profes
    template_name = "app_profes/profes_buscar.html"
    
    # para no usar el object_list que viene by default en el template uso
    context_object_name ='db_profes'

# Info de profes (Ver)
class InfoProfe(DetailView):
    model = Profes
    template_name = "app_profes/profe_info.html"
    # context_object_name = 'profe' no es necesario poner esto porque internamente 
    # django genera el contect_object_name como el nombre del modelo pero en minuscula

# No quiero que cualquiera pueda crear/modificar/eliminar profe. Sólo los usuarios logueados

# Creación de un nuevo profesor
class CrearProfe(LoginRequiredMixin,CreateView):
    model = Profes  # eso viene del model, entonces se trae igual
    template_name = "app_profes/profe_nuevo.html"
    fields = ['nombre', 'apellido', 'certificacion', 'horas_semana', 'fecha_ingreso', 'foto']   # los campos de mi formulario
    success_url = reverse_lazy('app_profes:profes_buscar')
     
# Modificar profes (Editar)
class UpdateProfe(LoginRequiredMixin, UpdateView):
    model = Profes
    template_name = "app_profes/profe_update.html"
    fields = ['nombre', 'apellido', 'certificacion', 'horas_semana', 'fecha_ingreso', 'foto']
    success_url = reverse_lazy('app_profes:profes_buscar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar el objeto profe al contexto
        context['profe'] = self.get_object()
        return context

# Borrar profes (Delete)
class BorrarProfe(LoginRequiredMixin, DeleteView):
    model = Profes
    template_name = "app_profes/profe_borrar.html"
    success_url = reverse_lazy('app_profes:profes_buscar')
    
    