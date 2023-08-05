from django.core.validators import MinValueValidator

from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField(null=False, blank=False)
    turno = models.IntegerField(null=False, default=2)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self):
        return f"{self.nombre}"
    
    
class Familiar(models.Model):
    ROLES = (
        ('yo', 'Yo'),
        ('hijo', 'Hijo'),
        ('padre', 'Padre'),
        ('madre', 'Madre'),
        ('abuelo_paterno', 'Abuelo Paterno'),
        ('abuela_paterna', 'Abuela Paterna'),
        ('abuelo_materno', 'Abuelo Materno'),
        ('abuela_materna', 'Abuela Materna'),
    )
    nombre = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    edad_de_matrimonio = models.IntegerField(null=True, blank=True)
    fecha_de_nacimiento = models.DateField()
    padres = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="hijos")
    rol = models.CharField(max_length=15, choices=ROLES, default='yo')
    
    
