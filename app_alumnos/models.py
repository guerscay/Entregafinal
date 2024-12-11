from django.db import models

class Alumnos(models.Model): #Creo una clase X, pero con herencia models.Model
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    anio_nacimiento = models.IntegerField()
    email = models.CharField(max_length = 30)
    
    def __str__(self):
        return f'Auto({self.id}): {self.nombre} {self.apellido}'