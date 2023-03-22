from django.urls import path
from Blog.views import *

app_name = 'Blog'

urlpatterns = [
    path('',inicio , name='inicio'),
    
]
