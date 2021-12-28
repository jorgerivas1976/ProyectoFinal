from django import forms
import datetime


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