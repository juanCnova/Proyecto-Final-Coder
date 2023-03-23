from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class PosteoForm(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=20)
    post = forms.CharField(max_length=20)
    imagen = forms.ImageField()

  
  
    