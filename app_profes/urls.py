from django.urls import path
from app_profes import views

app_name = 'app_profes'

urlpatterns = [
    path('profes/', views.VerProfes.as_view(), name = 'profes_buscar')
    
    
    
    
]