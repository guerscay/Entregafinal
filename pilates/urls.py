
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_alumnos.urls')),    #, nombre de la funcion en views
    path('', include('app_profes.urls')), # quiero que el acceso esté en profes, a las urls de app profes
    path('', include('app_acceso.urls')),
    path('',include('app_muro.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
