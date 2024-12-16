from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def acceso_login(request):
    
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('app_alumnos:home_login')
    
    
    return render(request, 'app_acceso/acceso_login.html', {'form' : form} )
