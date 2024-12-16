from django.urls import path
from app_acceso import views
from django.contrib.auth.views import LogoutView

app_name = 'app_acceso'

urlpatterns = [
    path ('login/', views.acceso_login, name = 'acceso_login'),
    path ('logout/', LogoutView.as_view(template_name = 'app_acceso/acceso_logout.html'), name = 'acceso_logout')
]
