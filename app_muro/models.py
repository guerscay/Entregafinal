from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.autor.username} - {self.fecha_publicacion.strftime('%Y-%m-%d %H:%M:%S')}"
