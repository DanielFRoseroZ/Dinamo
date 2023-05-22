from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre  
    

class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_lenght=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    id_rol = models.ForeignKey(Rol)
    sucursal = models.ForeignKey(Sucursal)
    
    def __str__(self):
        return self.nombre