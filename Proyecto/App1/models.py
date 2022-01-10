from django.db import models
from django.contrib.auth.models import User


class Bibliotecas (models.Model):
     ubicacion = models.CharField(max_length=60)
     nroAsociados = models.IntegerField()
     
     def __str__(self):
        
        return f"BIBLIOTECAS: {self.ubicacion} \ ASOCIADOS: {self.nroAsociados}"   

class Libros (models.Model):
    genero = models.CharField(max_length=40)
    nombre = models.CharField(max_length=50)
    numeroId = models.IntegerField()
    
    def __str__(self):
        
        return f"GENERO: {self.genero}  \ NOMBRE: {self.nombre} \ ID nro: {self.numeroId}"

class Asociados (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nroCarnet = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        
        return f"ASOCIADOS: {self.nombre} \ APELLIDO: {self.apellido} \ CARNET: {self.nroCarnet} \ EMAIL: {self.email}"


class Avatar (models.Model):

      user = models.ForeignKey(User, on_delete=models.CASCADE)

      imagen = models.ImageField(upload_to= 'avatares' , null=True , blank=True )     

