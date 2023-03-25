from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone



from Blog.forms import *
from Blog.models import *


# Create your views here.

def inicio(request):
    return render(request , 'Blog/inicio.html')

@login_required
def post(request):
    return render(request , 'Blog/post.html' )

@login_required
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
    return render(request , 'Blog/about.html')


class BlogList(LoginRequiredMixin,ListView):
    model = Posteo
    template_name = 'Blog/blogList.html'

class BlogDetail(LoginRequiredMixin , DetailView):
    model = Posteo
    template_name = 'Blog/blogDetail.html'

class BlogDelete(LoginRequiredMixin , DeleteView):
    model = Posteo
    template_name = 'Blog/post_confirm_delete.html'
    success_url = reverse_lazy('Blog:blogList')


@login_required
def editarPost(request, titulo_post):
    

    post = Posteo.objects.get(titulo=titulo_post)
    if request.user == post.autor:


        if request.method == 'POST':

            formulario = PosteoForm(request.POST , request.FILES)

            if formulario.is_valid():  

                info = formulario.cleaned_data

                post.autor = request.user
                post.titulo = info['titulo']
                post.subtitulo = info['subtitulo']
                post.post = info['post']
                post.fecha = timezone.now()

                if info['imagen'] != None:
                    post.imagen = info['imagen'] 

                post.save()

                return render(request, "Blog/post.html")

        else:
        
            formulario = PosteoForm(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo,'post': post.post, 'autor': post.autor , 'imagen': post.imagen})

    
        return render(request, "blog/newPost.html", {"formulario": formulario, "titulo_post": titulo_post})
    
    else:
        return PermissionError

@login_required
def formBusqueda(request):
    return render(request , 'Blog/formBusqueda.html')

@login_required
def resultadoBusqueda(request):
    post = None # Valor predeterminado para evitar el error UnboundLocalError
   
    if 'titulo' in request.GET:
        titulo = request.GET['titulo']
        post = Posteo.objects.filter(titulo__icontains=titulo)

        if len(titulo) == 0:
              return render(request , 'Blog/resultados.html', {'vacio':1})

    elif 'autor' in request.GET:
        autor = request.GET['autor']
        post = Posteo.objects.filter(autor__username__icontains=autor)

        if len(autor) == 0:
              return render(request , 'Blog/resultados.html', {'vacio':1})

    else:
        return HttpResponse('No se ingresaron datos')

    return render(request , 'Blog/resultados.html', {'post':post})
