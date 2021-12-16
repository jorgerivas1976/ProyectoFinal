from django.http import request

from django.shortcuts import render

from App1.models import *

 

def inicio (request):
     
    return render(request, "App1/inicio.html")

def bibliotecas(request):
     
    return render(request, "App1/bibliotecas.html")

def libros(request):
     
    return render(request, "App1/libros.html")

def asociados(request):
     
    return render(request, "App1/asociados.html")


def bibliotecasFormulario(request):
     
     if request.method == "POST":
         
         bibliotecas = Bibliotecas(ubicacion=request.POST["ubicacion"], nroAsociados=request.POST["nroAsociados"])
         
         bibliotecas.save()
         
         return render(request, "App1/inicio.html")
         
     
     return render(request, "App1/bibliotecasFormulario.html")
 
 
def librosFormulario(request):
     
     if request.method == "POST":
         
         libros = Libros(genero=request.POST["genero"], nombre=request.POST["nombre"], numeroId=request.POST["numeroId"])
         
         libros.save()
         
         return render(request, "App1/inicio.html")
         
     
     return render(request, "App1/librosFormulario.html")
 
 
def asociadosFormulario(request):
     
     if request.method == "POST":
         
         asociados = Asociados(nombre=request.POST["nombre"], apellido=request.POST["apellido"], nroCarnet=request.POST["nroCarnet"], email=request.POST["email"])
         
         asociados.save()
         
         return render(request, "App1/inicio.html")
         
     
     return render(request, "App1/asociadosFormulario.html")