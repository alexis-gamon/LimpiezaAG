from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Encargado(models.Model):
    Nombre = models.CharField(max_length=50)

    
def __str__(self):
        return self.Nombre



class Supervisor(models.Model):

    Nombre = models.CharField(max_length=50)

    Limpio = models.TextField(max_length=3)

    

class Administrador(models.Model):
    Nombre = models.TextField(max_length=50)

    Autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    Clave = models.PositiveIntegerField(null = True, blank = True)

    Hora = models.PositiveIntegerField(null = True, blank = True)

    Fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('limpieza_detalle', args=(str(self.id)))


class Comentario(models.Model):
    Administrador = models.ForeignKey(
        Administrador,
        on_delete=models.CASCADE,
        related_name='comentarios',

    )
    comentario = models.CharField(max_length=200)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('lista_tec')


