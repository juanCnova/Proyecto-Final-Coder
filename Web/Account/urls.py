from django.urls import path
from Account.views import *

app_name = 'Account'

urlpatterns = [
    path('',Account , name='account'),
    path('login/',login_user , name='login'),
    path('register/',register , name='register'),
    
]
