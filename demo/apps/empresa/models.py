from django.db import models
from apps.user.models import User


# Modelo Departamento
class Depto(models.Model):
    nombreDepto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    empleados = models.ManyToManyField(User, related_name='empleado')
    
    def __str__(self):
        return self.nombreDepto


# Modelo Empresa
class Empresa(models.Model):
    nombreEmp = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    deptos = models.ManyToManyField(Depto, blank=False)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
