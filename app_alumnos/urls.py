from django.contrib import admin
from django.urls import path
from app_alumnos import views

app_name = 'app_alumnos'

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('welcome', bienvenida), 
    path('', views.home, name = 'home'),
    path('login', views.home_login, name = 'home_login'),
    path('alumnos/crear/', views.alumno_nuevo, name = 'alumno_nuevo'),
    path('alumnos/', views.alumno_buscar, name = 'alumno_buscar'),
    path('alumnos/<int:id_alumno>', views.alumno_ver, name = 'alumno_ver'),
    path('alumnos/<int:id_alumno>/editar', views.alumno_editar, name = 'alumno_editar'),
    path('alumnos/<int:id_alumno>/eliminar', views.alumno_eliminar, name = 'alumno_eliminar'),
]
