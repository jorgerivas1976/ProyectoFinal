from django.urls import path
from App1 import views

urlpatterns = [
    
 path('inicio', views.inicio, name="Inicio"),
 path('bibliotecas', views.bibliotecas, name="Bibliotecas"),
 path('libros', views.libros, name="Libros"),
 path('asociados', views.asociados, name="Asociados"),
 path('bibliotecasFormulario', views.bibliotecasFormulario, name="BibliotecasFormulario"),
    
]