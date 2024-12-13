
from django.contrib import admin
from django.urls import path, include
#from app_alumnos.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_alumnos.urls')),    #, nombre de la funcion en views
    path('profes/', include('app_profes.urls')) # quiero que el acceso esté en profes, a las urls de app profes
]
