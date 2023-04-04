from django.db import models

class Prueba(models.Model):
   titulo = models.CharField(max_length=50)
   subtitulo = models.CharField(max_length=50)
   cantidad = models.IntegerField()
