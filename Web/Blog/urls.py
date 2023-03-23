from django.urls import path
from Blog.views import *

app_name = 'Blog'

urlpatterns = [
    path('',inicio , name='inicio'),
    path('post/',post , name='post'),
    path('about/',about , name='about'),
    path('newPost/',newPost , name='newPost'),
    
]
