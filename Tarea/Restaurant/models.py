from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre

class Hamburgesa(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(default=7)
    descripcion = models.CharField(max_length=300)
    imagen = models.CharField(max_length=200)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nombre


