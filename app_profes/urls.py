from django.urls import path
from app_profes import views

app_name = 'app_profes'

urlpatterns = [
    path('profes/', views.ListaProfes.as_view(), name = 'profes_buscar'),
    path('profes/crear', views.CrearProfe.as_view(), name = 'profe_nuevo'),
    path('profes/info/<int:pk>', views.InfoProfe.as_view(), name = 'profe_info'),
    path('profes/edit/<int:pk>', views.UpdateProfe.as_view(), name='profe_update')
]
