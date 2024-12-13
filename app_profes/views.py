from django.shortcuts import render
from django.views.generic.list import ListView
from app_profes.models import Profes

class VerProfes(ListView):
    model = Profes
    template_name = "app_profes/profes_buscar.html"
    
    # para no usar el object_list que viene by default en el template uso
    context_object_name ='db_profes'


# Create your views here.
