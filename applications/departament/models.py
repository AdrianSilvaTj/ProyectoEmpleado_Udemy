from django.db import models

class Departament(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado',default=False)
    
    class Meta:
        ordering = ['name']
        managed = True
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        unique_together = ('name','short_name')
    
    def __str__(self):
        return self.short_name