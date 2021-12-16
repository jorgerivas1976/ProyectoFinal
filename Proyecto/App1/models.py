from django.db import models


class Bibliotecas (models.Model):
     ubicacion = models.CharField(max_length=60)
     nroAsociados = models.IntegerField()

class Libros (models.Model):
    genero = models.CharField(max_length=40)
    nombre = models.CharField(max_length=50)
    numeroId = models.IntegerField()

class Asociados (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nroCarnet = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        
        return f"ASOCIADOS: {self.nombre} APELLIDO: {self.apellido} CARNET: {self.nroCarnet} EMAIL: {self.email} "


    