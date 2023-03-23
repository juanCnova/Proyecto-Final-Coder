from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from Account.forms import *
from Account.models import *
from django.contrib.auth.decorators import login_required 


# Create your views here.

@login_required
def perfil(request):
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

                avatares = Avatar.objects.filter(user=request.user.id).first()
                print(avatares)
                if avatares is not None:
                    avatares_url = avatares.imagen.url
                else:
                    avatares_url = None

                
                msj = f'Bienvenido {request.user}' 

                return render(request, 'Blog/inicio.html' , {'msj':msj , 'url':avatares_url})
            else:
                return HttpResponse('error de usuario')
        
        else:
            return HttpResponse('error de formulario')

    else:
        formulario = loginForm()
        return render(request, 'Account/login.html', {"formulario": formulario})



def register(request):
    
    if request.method =='POST':
        
        formulario = UserRegister(request.POST)

        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            messages.success(request, 'Tu cuenta ha sido creada! Ahora puedes iniciar sesión')

            return render(request , 'Blog/inicio.html' , {'msj':'Usuario creado correctamente'})
        else:
            return render(request , 'Account/register.html' , {'msj':'Error al crear usuario'})
        

    else:
        formulario = UserRegister()

    return render(request, 'Account/register.html' , {'formulario':formulario})

def agregarAvatar(request):
    if request.method == 'POST':
        formulario = avatarForm(request.POST , request.FILES)
        
        if formulario.is_valid():
            
            
            try:
               avatar = Avatar.objects.get(user = request.user)
               avatar.delete()
            except:
                avatar = Avatar(user = request.user , imagen = formulario.cleaned_data['imagen']) 
                avatar.save()

                
            
            avatar = Avatar(user = request.user , imagen = formulario.cleaned_data['imagen']) 
            avatar.save()
            
            return render(request , 'Blog/inicio.html')

    else:
        formulario = avatarForm()
    
    return render(request, 'Account/editarAvatar.html' , {'formulario':formulario})