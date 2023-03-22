from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request , 'Blog/inicio.html')

def post(request):
    return render(request , 'Blog/post.html')

def about(request):
    return render(request ,  'Blog/about.html')
