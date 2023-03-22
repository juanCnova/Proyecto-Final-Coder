from django.urls import path
from Account.views import *
from django.contrib.auth.views import LogoutView

app_name = 'Account'

urlpatterns = [
    path('',Account , name='account'),
    path('login/',login_user , name='login'),
    path('register/',register , name='register'),
    path('logout/',LogoutView.as_view(template_name = 'Blog/inicio.html') , name='logout'),
    
]
