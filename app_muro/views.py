from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mensaje

class MuroVer(ListView):
    model = Mensaje
    template_name = "app_muro/muro_ver.html"
    context_object_name = "mensajes"
    ordering = ['-fecha_publicacion']  # Ordenar los mensajes del más reciente al más antiguo

class MuroEscribir(LoginRequiredMixin, CreateView):
    model = Mensaje
    template_name = "app_muro/muro_escribir.html"
    fields = ['contenido']
    success_url = reverse_lazy('app_muro:muro_ver')  # Redirigir al muro después de enviar un mensaje

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asignar el autor al usuario autenticado
        return super().form_valid(form)
