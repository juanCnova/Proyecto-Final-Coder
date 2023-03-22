from django.urls import path
from Account.views import *

app_name = 'Account'

urlpatterns = [
    path('Login/',login , name='login'),
    
]
