from django.db import models
from applications.departament.models import Departament
from ckeditor.fields import RichTextField

class Skill(models.Model):
    name = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        ordering = ['name']        
        verbose_name = 'Habilidad Empleado'
        verbose_name_plural = 'Habilidades Empleado'
        
    def __str__(self):
        return self.name
        

class Employee(models.Model):
    
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'DESARROLLADOR'),        
        ('4', 'ALMACENISTA'),        
        ('5', 'TÉCNICO'),        
        ('6', 'ENFERMERA'),        
        ('7', 'OTRO'),        
    )
    
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Cargo', max_length=1, choices=JOB_CHOICES)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    # Crear relación Muchos a Muchos con 'Skill'
    skills= models.ManyToManyField(Skill, verbose_name='Habilidades')
    cv = RichTextField()
    
    class Meta:
        ordering = ['last_name']        
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        
    def __str__(self):
        return str(self.id)+' '+self.first_name + ' ' + self.last_name
