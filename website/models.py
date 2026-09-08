from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnolgia = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo