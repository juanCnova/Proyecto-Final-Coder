from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout , authenticate
from Account.forms import *

# Create your views here.

def Account(request):
    return render(request, 'Account/perfil.html')

def login_user(request):
    
    if  request.method == "POST":

        formulario = loginForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            username = data.get('username')
            password = data.get('password')
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                msj = f'Bienvenido {request.user}' 

                return render(request, 'Blog/inicio.html' , {'msj':msj})
            else:
                return HttpResponse('error de usuario')
        
        else:
            return HttpResponse('error de formulario')

    else:
        formulario = loginForm()
        return render(request, 'Account/login.html', {"formulario": formulario})



def register(request):
    return render(request, 'Account/register.html')
