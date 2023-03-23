from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':"password-field" , 'type':"password" , 'class':"form-control" , 'placeholder':"Password"}))

class UserRegister(UserCreationForm):
    username = forms.CharField(min_length=4,max_length=15 ,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '' , 'name':"username" , 'type':'text'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
    password1 = forms.CharField(min_length= 6 ,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))
    password2 = forms.CharField(min_length = 6 ,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        field_order = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
class avatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']
    
