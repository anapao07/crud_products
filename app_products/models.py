from django.db import models

# Create your models here.
class Products(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre
        