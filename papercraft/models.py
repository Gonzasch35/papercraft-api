from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Modelo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.FileField(default='')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='modelo_categoria')
    alto = models.CharField(max_length=20)
    ancho = models.CharField(max_length=20)
    profundidad = models.CharField(max_length=20)
    piezas = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name