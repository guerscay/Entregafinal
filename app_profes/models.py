from django.db import models

class Profes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    certificacion = models.CharField(max_length=200)
    horas_semana = models.IntegerField()
    fecha_ingreso = models.DateField()
    foto = models.ImageField(upload_to = 'app_profes', blank = True, null=True)
    
    def __str__(self):
            return f' Profe ({self.id}): {self.nombre} {self.apellido}' 