from django.urls import path
from .views import MuroEscribir, MuroVer

app_name = 'app_muro'

urlpatterns = [
    path('muro/', MuroVer.as_view(), name = 'muro_ver'),
    path('muro/escribir/', MuroEscribir.as_view(), name = 'muro_escribir'),
    ]