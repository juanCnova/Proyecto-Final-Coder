from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class PosteoForm(forms.Form):
    
    titulo = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control', 'name':"titulo" , 'type':'text'}))
    subtitulo = forms.CharField(max_length=35 ,widget=forms.TextInput(attrs={'class': 'form-control', 'name':"subtitulo" , 'type':'text'}))
    post = forms.CharField(max_length=200 ,widget=forms.Textarea(attrs={ 'rows':5  ,'class': 'form-control', 'name':"post" , 'type':'text'}))
    imagen = forms.ImageField(required=False , widget=forms.FileInput(attrs={'class': 'form-control', 'name':"imagen" , 'type':'FILE'}))
  
  
    