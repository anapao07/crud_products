from django.db import models

# Create your models here.
class Products(models.Model):
    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=7, unique=True)
    precio = models.IntegerField()
    existencia = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nombre
