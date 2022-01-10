from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
 
 path('inicio', views.inicio, name="Inicio"),
 path('bibliotecas', views.bibliotecas, name="Bibliotecas"),
 path('libros', views.libros, name="Libros"),
 path('asociados', views.asociados, name="Asociados"),
 
 path('bibliotecasFormulario', views.bibliotecasFormulario, name="BibliotecasFormulario"),
 path('librosFormulario', views.librosFormulario, name="LibrosFormulario"),   
 path('asociadosFormulario', views.asociadosFormulario, name="AsociadosFormulario"),   
 
 path('busquedaBiblioteca', views.busquedaBiblioteca),
 path('buscar/', views.buscar),
 path('busquedaAsociados', views.busquedaAsociados),
 path('buscarAsociados/', views.buscarAsociados),
 path('busquedaLibros', views.busquedaLibros),
 path('buscarLibros/', views.buscarLibros),

 path('leerBibliotecas', views.leerBibliotecas, name="LeerBibliotecas"),
 path('leerLibros', views.leerLibros, name="LeerLibros"),
 path('leerAsociados', views.leerAsociados, name="LeerAsociados"),
 
 path('eliminarBibliotecas/<ubicacion_para_borrar>/', views.eliminarBibliotecas, name="EliminarBibliotecas"),
 path('eliminarLibros/<nombre_para_borrar>/', views.eliminarlibros, name="EliminarLibros"),
 path('eliminarAsociados/<nombre_para_borrar>/', views.eliminarAsociados, name="EliminarAsociados"),
 
 path('editarBibliotecas/<ubicacion_para_editar>/', views.editarBibliotecas, name="EditarBibliotecas"),
 path('editarAsociados/<nombre_para_editar>/', views.editarAsociados, name="EditarAsociados"),
 path('editarLibros/<nombre_para_editar>/', views.editarLibros, name="EditarLibros"),
 
 path('libros/list', views.LibrosList.as_view(), name='List'), 
 path(r'^(?P<pk>\d+)$', views.LibrosDetalle.as_view(), name='Detail'),   
 path(r'^nuevo$', views.LibrosCreacion.as_view(), name='New'),
 path(r'^editar/(?P<pk>\d+)$', views.LibrosUpdate.as_view(), name='Edit'),
 path(r'^borrar/(?P<pk>\d+)$', views.LibrosDelete.as_view(), name='Delete'),
 
 path('login', views.login_request, name="Login"),
 path('register', views.register, name="Register"),
 path('logout', LogoutView.as_view(template_name='App1/logout.html'), name="Logout"),
 
 path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
 
]