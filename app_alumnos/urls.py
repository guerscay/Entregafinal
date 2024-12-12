from django.contrib import admin
from django.urls import path
from app_alumnos import views

app_name = 'app_alumnos'

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('welcome', bienvenida), 
    path('', views.home, name = 'home'),
    path('alumnos/crear/', views.alumno_nuevo, name = 'alumno_nuevo'),
    path('alumnos/', views.alumno_buscar, name = 'alumno_buscar'),
    path('alumnos/<int:id_alumno>', views.alumno_ver, name = 'alumno_ver'),
]
