from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Etiquetas(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='proyectos', null=True, blank=True
    )
    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='proyectos',
        null=True,
        blank=True,
    )
    etiquetas = models.ManyToManyField(
        Etiquetas,
        related_name='proyectos',
        blank=True
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='proyectos',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo