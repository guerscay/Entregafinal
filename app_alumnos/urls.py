from django.contrib import admin
from django.urls import path
from app_alumnos import views

app_name = 'app_alumnos'

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('welcome', bienvenida), 
    path('', views.home, name = 'home'),
    path('alumno_nuevo/', views.alumno_nuevo, name = 'alumno_nuevo'),
    path('alumno_buscar/', views.alumno_buscar, name = 'alumno_buscar'),
]
