from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BibliotecasFormulario(forms.Form):
    
    ubicacion = forms.CharField(required=True)
    nroAsociados = forms.IntegerField()
    
class LibrosFormulario(forms.Form):
    genero = forms.CharField(max_length=40)
    nombre = forms.CharField(max_length=50)
    numeroId = forms.IntegerField()   
    
class AsociadosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nroCarnet = forms.IntegerField()
    email = forms.EmailField()
    
    
class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        
class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 


class AvatarFormulario(forms.Form):

    imagen = forms.ImageField(required=True)
