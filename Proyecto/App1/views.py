from django.http import request

from django.shortcuts import render

from App1.models import *

from App1.forms import *

from django.http import HttpResponse

 

def inicio (request):
     
    return render(request, "App1/inicio.html")


def bibliotecas(request):
     
    return render(request, "App1/bibliotecas.html")


def libros(request):
     
    return render(request, "App1/libros.html")


def asociados(request):
     
    return render(request, "App1/asociados.html")


#API forms
def bibliotecasFormulario(request):
     
     if request.method == "POST":
         
         miFormulario = BibliotecasFormulario(request.POST)
         
         if miFormulario.is_valid():
             
             informacion = miFormulario.cleaned_data
             
             biblioteca = Bibliotecas(
                 
                 ubicacion = informacion['ubicacion'],
                 nroAsociados = informacion['nroAsociados']
                                 
             )
             
             biblioteca.save()
         
         return render(request, "App1/inicio.html")
     
     else:
         
         miFormulario = BibliotecasFormulario()    
     
     return render(request, "App1/bibliotecasFormulario.html", {"miFormulario":miFormulario})
 

 
def librosFormulario(request):
     
     if request.method == "POST":
         
         miFormulario = LibrosFormulario(request.POST)
         
         if miFormulario.is_valid():
             
             informacion = miFormulario.cleaned_data
             
             libro = Libros(
                 
                 genero = informacion['genero'],
                 nombre = informacion['nombre'],
                 numeroId = informacion['numeroId']
                
             )        
             
             libro.save()
             
         return render(request, "App1/inicio.html")
     
     else:
         
         miFormulario = LibrosFormulario()
         
     
     return render(request, "App1/librosFormulario.html", {"miFormulario":miFormulario})
 

 
def asociadosFormulario(request):
     
     if request.method == "POST":
         
         miFormulario = AsociadosFormulario(request.POST)
         
         if miFormulario.is_valid():
             
             informacion = miFormulario.cleaned_data
             
             socio = Asociados(
                 
                 nombre = informacion['nombre'],
                 apellido = informacion['apellido'],
                 nroCarnet = informacion['nroCarnet'],
                 email = informacion['email']
                 
             )
         
             socio.save()
         
         return render(request, "App1/inicio.html")
         
     else:
         
         miFormulario = AsociadosFormulario()
     
     
     return render(request, 'App1/asociadosFormulario.html', {"miFormulario":miFormulario})
 
 
 #Buscar
def busquedaBiblioteca(request):
    
    return render(request, 'App1/busquedaBiblioteca.html')

def buscar(request):
    
    if request.GET["ubicacion"]:
        
        ubicacion = request.GET["ubicacion"]
        
        bibliotecas = Bibliotecas.objects.filter(ubicacion__icontains=ubicacion)
        
        return render(request, "App1/resultadoBusqueda.html",{"ubicacion":ubicacion, "bibliotecas":bibliotecas})
                 
    else: 
        
        respuesta = "Por favor, ingrese los datos: "     
    
    return HttpResponse(respuesta)



