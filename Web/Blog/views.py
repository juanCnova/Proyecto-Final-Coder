from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 


# Create your views here.

def inicio(request):
    return render(request , 'Blog/inicio.html')

@login_required
def post(request):
    return render(request , 'Blog/post.html')

def about(request):
    return render(request ,  'Blog/about.html')
