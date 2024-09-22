from django.db import models
from django.contrib.auth.models import User

class Camiseta(models.Model):
    name = models.CharField(max_length=50)
    talle = models.CharField(max_length=3)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    nombre_vendedor = models.CharField(max_length=100, null=True, blank=True)
    numero_contacto = models.CharField(max_length=15, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        return self.name

class Short(models.Model):
    name = models.CharField(max_length=50)
    talle = models.CharField(max_length=3)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    nombre_vendedor = models.CharField(max_length=100, null=True, blank=True)
    numero_contacto = models.CharField(max_length=15, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        return self.name

class Botin(models.Model):
    name = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    nombre_vendedor = models.CharField(max_length=100, null=True, blank=True)
    numero_contacto = models.CharField(max_length=15, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        return self.name
