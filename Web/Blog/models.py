from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Posteo(models.Model):
    autor = models.ForeignKey(User , on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    post = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='img' , null = True , blank = True)

    def __str__(self):
        return f'{self.titulo} by {self.autor}'