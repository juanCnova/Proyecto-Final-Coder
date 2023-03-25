from django.urls import path
from Blog.views import *

app_name = 'Blog'

urlpatterns = [
    path('',inicio , name='inicio'),
    path('post/',post , name='post'),
    path('about/',about , name='about'),
    path('newPost/',newPost , name='newPost'),
    path('post/list/',BlogList.as_view() , name='blogList'),
    path('post/<int:pk>/', BlogDetail.as_view(), name='detalle'),
    path('post/borrar/<int:pk>', BlogDelete.as_view() , name = 'delete'),
    path('editarPost/<titulo_post>', editarPost , name = 'editarPost'),
    path('post/buscarPost/', formBusqueda , name = 'buscar'),
    path('post/resultadoBusqueda/', resultadoBusqueda , name = 'resultado'),



    
]
