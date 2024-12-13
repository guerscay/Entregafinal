from django.shortcuts import render
from django.views.generic.list import ListView
from app_profes.models import Profes

class VerProfes(ListView):
    model = Profes
    template_name = "app_profes/profes_buscar.html"


# Create your views here.
