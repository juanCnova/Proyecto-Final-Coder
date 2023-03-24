from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
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

class BlogList(ListView):
    model = Posteo
    template_name = 'Blog/blogList.html'

class BlogDetail(DetailView):
    model = Posteo
    template_name = 'Blog/blogDetail.html'

class BlogDelete(DeleteView):
    model = Posteo
    template_name = 'Blog/post_confirm_delete.html'
    success_url = reverse_lazy('Blog:blogList')

def editarPost(request, titulo_post):

    post = Posteo.objects.get(titulo=titulo_post)

    if request.method == 'POST':

        formulario = PosteoForm(request.POST , request.FILES)

        if formulario.is_valid():  

            info = formulario.cleaned_data

            post.autor = request.user
            post.titulo = info['titulo']
            post.subtitulo = info['subtitulo']
            post.post = info['post']
            post.imagen = info['imagen']
            post.fecha = timezone.now()

            post.save()

            return render(request, "Blog/post.html")

    else:
        
        formulario = PosteoForm(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo,'post': post.post, 'autor': post.autor , 'imagen': post.imagen})

    
    return render(request, "blog/newPost.html", {"formulario": formulario, "titulo_post": titulo_post})