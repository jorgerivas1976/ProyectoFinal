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