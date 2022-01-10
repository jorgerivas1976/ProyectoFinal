
from django.http import request

from django.shortcuts import render

from App1.models import *

from App1.forms import *

from django.http import HttpResponse

from App1.views import *

from django.views.generic import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import  CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required


def inicio (request):
     
    return render(request, "App1/inicio.html")


def bibliotecas(request):
     
    return render(request, "App1/bibliotecas.html")


def libros(request):
     
    return render(request, "App1/libros.html")


def asociados(request):
     
    return render(request, "App1/asociados.html")


#API forms / CRUD

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
 
 #BUSQUEDA
 
def busquedaAsociados(request):
    
    return render(request, 'App1/busquedaAsociados.html')

def busquedaLibros(request):
    
    return render(request, 'App1/busquedaLibros.html')

def busquedaBiblioteca(request):
    
    return render(request, 'App1/busquedaBiblioteca.html')

def buscarAsociados(request):
    
    if request.GET["apellido"]:
        
        apellido = request.GET["apellido"]
        
        asociados = Asociados.objects.filter(apellido__icontains=apellido)
        
        return render(request, "App1/resultadoBusquedaAsociados.html",{"apellido":apellido, "asociados":asociados})
                 
    else: 
        
        respuesta = "Por favor, ingrese los datos: "     
    
    return HttpResponse(respuesta)

def buscarLibros(request):
    
    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        
        libros = Libros.objects.filter(nombre__icontains=nombre)
        
        return render(request, "App1/resultadoBusquedaLibros.html",{"nombre":nombre, "libros":libros})
                 
    else: 
        
        respuesta = "Por favor, ingrese los datos: "     
    
    return HttpResponse(respuesta)

def buscar(request):
    
    if request.GET["ubicacion"]:
        
        ubicacion = request.GET["ubicacion"]
        
        bibliotecas = Bibliotecas.objects.filter(ubicacion__icontains=ubicacion)
        
        return render(request, "App1/resultadoBusqueda.html",{"ubicacion":ubicacion, "bibliotecas":bibliotecas})
                 
    else: 
        
        respuesta = "Por favor, ingrese los datos: "     
    
    return HttpResponse(respuesta)


@login_required
def leerBibliotecas(request):
    
    bibliotecas = Bibliotecas.objects.all()
    
    dir = {"bibliotecas":bibliotecas} 
    
    return render(request, "App1/leerBibliotecas.html", dir)


def leerLibros(request):
    
    libros = Libros.objects.all()
    
    dir = {"libros":libros} 
    
    return render(request, "App1/leerLibros.html", dir)


def leerAsociados(request):
    
    asociados = Asociados.objects.all()
    
    dir = {"asociados":asociados} 
    
    return render(request, "App1/leerAsociados.html", dir)



def eliminarBibliotecas(request, ubicacion_para_borrar):
    
    bibliotecasABorrar = Bibliotecas.objects.get(ubicacion=ubicacion_para_borrar)
    bibliotecasABorrar.delete()
    
    bibliotecas = Bibliotecas.objects.all()
    
    return render(request, "App1/leerBibliotecas.html", {"bibliotecas":bibliotecas})


def eliminarlibros(request, nombre_para_borrar):
    
    librosABorrar = Libros.objects.get(genero=nombre_para_borrar)
    librosABorrar.delete()
    
    libros = Libros.objects.all()
    
    return render(request, "App1/leerLibros.html", {"libros":libros})


def eliminarAsociados(request, nombre_para_borrar):
    
    asociadosABorrar = Asociados.objects.get(nombre=nombre_para_borrar)
    asociadosABorrar.delete()
    
    asociados = Asociados.objects.all()
    
    return render(request, "App1/leerAsociados.html", {"asociados":asociados})



def editarBibliotecas(request, ubicacion_para_editar): 
    
    biblioteca = Bibliotecas.objects.get(ubicacion=ubicacion_para_editar)
    
    if request.method == "POST":
        
        miFormulario = BibliotecasFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            biblioteca.ubicacion = informacion["ubicacion"]
            biblioteca.nroAsociados = informacion["nroAsociados"]
                      
            biblioteca.save() 
            
            return render(request, "App1/inicio.html")
       
    else:
        
        miFormulario = BibliotecasFormulario(initial={"ubicacion":biblioteca.ubicacion,"nroAsociados":biblioteca.nroAsociados})
 
    return render(request, "App1/editarBibliotecas.html",{"miFormulario":miFormulario,"ubicacion_para_editar":ubicacion_para_editar})


def editarAsociados(request, nombre_para_editar): 
    
    asociado = Asociados.objects.get(nombre=nombre_para_editar)
    
    if request.method == "POST":
        
        miFormulario = AsociadosFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            asociado.nombre = informacion["nombre"]
            asociado.apellido = informacion["apellido"]
            asociado.nroCarnet = informacion["nroCarnet"]
            asociado.email = informacion["email"]
                      
            asociado.save() 
            
            return render(request, "App1/inicio.html")
       
    else:
        
        miFormulario = AsociadosFormulario(initial={"nombre":asociado.nombre,"apellido":asociado.apellido,"nroCarnet":asociado.nroCarnet,"email":asociado.email})
 
    return render(request, "App1/editarAsociados.html",{"miFormulario":miFormulario,"nombre_para_editar":nombre_para_editar})

def editarLibros (request, nombre_para_editar): 
     
    libro = Libros.objects.get (nombre = nombre_para_editar)


    if request.method == "POST":
        
        miFormulario = LibrosFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            libro.nombre = informacion ["nombre"]
            libro.genero = informacion ["genero"]
            libro.numeroId = informacion ["numeroId"]

            libro.save()
            return render (request, "App1/inicio.html")

    else:
        miFormulario = LibrosFormulario(initial={"nombre":libro.nombre,"genero":libro.genero,"numeroId":libro.numeroId})
 
    return render (request, "App1/editarLibros.html",{"miFormulario":miFormulario,"nombre_para_editar":nombre_para_editar})                
    
    

#CBV
#LIBROS
class LibrosList(ListView):
    
    model = Libros
    template_name = "App1/libros_list.html"
    
class LibrosDetalle(DetailView):
    
    model = Libros
    template_name = "App1/libros_detalle.html"
    
class LibrosCreacion(CreateView):
    
    model = Libros
    success_url = "../libros/list"  
    fields = ["genero", "nombre", "numeroId"]
    
class LibrosUpdate(UpdateView):
    
    model = Libros
    success_url = "../libros/list"
    fields = ["genero", "nombre", "numeroId"]
   
class LibrosDelete(DeleteView):
    
    model = Libros
    success_url = "../libros/list"
    
    
#LOGIN/REGISTER/LOGOUT/EDITAR

def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido, {usuario}"})
                
            else:
                
                return render(request, "App1/inicio.html", {"mensaje":f"Datos erroneos"})
                
            
        else:
            
            return render(request, "App1/inicio.html", {"mensaje":f"Formulario erroneo"})
            
    
    form = AuthenticationForm()  
    
    return render(request, "App1/login.html", {"form":form} )



def register(request):

      if request.method == 'POST':
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                       
                  form.save()
                  
                  return render(request,"App1/inicio.html" ,  {"mensaje":f"{username} Creado"})

      else:          
              
            form = UserRegisterForm()     

      return render(request,"App1/register.html", {"form":form})
  


@login_required
def editarPerfil(request):
     
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
            return render(request, "App1/inicio.html")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
        
    return render(request, "App1/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
  

@login_required
def inicio (request):
     
     diccionario = {}
     cantidadDeAvatares = 0

     if request.user.is_authenticated:

        avatar = Avatar.objects.filter( user = request.user.id )
         
        for a in avatar:

             cantidadDeAvatares = cantidadDeAvatares + 1

        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url

        

     return render (request, "App1/inicio.html", diccionario)

@login_required
def agregarAvatar(request):
     
    
    if request.method == 'POST':
        
        miFormulario = AvatarFormulario(request.POST,request.FILES)
        
        if miFormulario.is_valid():
            
            u = User.objects.get(username=request.user)
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])
            
            avatar.save()
            
            return render(request, "App1/inicio.html")
        
    else:
        
        miFormulario = AvatarFormulario
        
        
    return render(request, "App1/agregarAvatar.html", {"miFormulario":miFormulario})




