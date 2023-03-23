from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from Blog.forms import *
from Blog.models import *


# Create your views here.

def inicio(request):
    return render(request , 'Blog/inicio.html')

@login_required
def post(request):
    return render(request , 'Blog/post.html' )

def newPost(request):
    if request.method == 'POST':
        formulario = PosteoForm(request.POST , request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data

            posteo = Posteo(autor = request.user , titulo = info['titulo'] , subtitulo = info['subtitulo'] , post = info['post'] , imagen = info['imagen'])
            posteo.save()

            return render(request, 'Blog/inicio.html')

    else:
        formulario = PosteoForm()

    return render(request , 'Blog/newPost.html' , {'formulario':formulario})
    
    

def about(request):
    return render(request ,  'Blog/about.html')
