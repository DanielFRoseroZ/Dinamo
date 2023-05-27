from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Rol' 
    

class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Sucursal'
        
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=50)
    nomre_producto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Proveedor'    

class Usuario(models.Model):
    cedula = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Usuario'
        
class Auto(models.Model):
    modelo = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    foto = cloudinary.models.CloudinaryField(folder='media/auto_images/', overwrite=True, resource_type='', blank=True)
    precio = models.IntegerField(default=0)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    año = models.CharField(max_length=10)
    caracteristicas = models.CharField(max_length=300)
    kilometraje = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.modelo
    
    class Meta:
        db_table = 'Auto'
        
class Repuesto(models.Model):
    articulo = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    proveedor = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    cantidadMinima = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.articulo
    
    class Meta:
        db_table = 'Repuesto'

class Cita(models.Model):
    fecha = models.CharField(max_length=200)
    nombre_empleado = models.CharField(max_length=100)
    cedula_empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cedula_empleado')
    nombre_cliente = models.CharField(max_length=100)
    cedula_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cedula_cliente')
    descripcion = models.CharField(max_length=400)
    
    def __str__(self):
        return self.fecha
    
    class Meta:
        db_table = 'Cita'
    
class Venta(models.Model):
    precio = models.IntegerField(default=0)
    nombre_vendedor = models.CharField(max_length=100)
    cedula_vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_venta = models.CharField(max_length=100)
    comentario = models.CharField(max_length=200)
    metodo_pago = models.CharField(max_length=50)
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_vendedor
        
    class Meta:
        db_table = 'Venta'    
    
class Pago(models.Model):
    tipo_pago = models.CharField(max_length=100)
    cantidad_pago = models.IntegerField(default=0)
    nombre_cliente = models.CharField(max_length=200)
    cedula_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    meotodo_pago = models.CharField(max_length=100)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_cliente
    
    class Meta:
        db_table = 'Pago'

class RegistroTaller(models.Model):
    placa_auto = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    comentario = models.CharField(max_length=200)
    fecha_ingreso = models.CharField(max_length=100)
    fecha_entregado = models.CharField(max_length=100)
    costo_reparacion = models.IntegerField(default=0)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    mecanico_encargado = models.CharField(max_length=100)
    cedula_mecanico = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.modelo
        
    class Meta:
        db_table = 'RegistroTaller'
    

        
class Credito(models.Model):
    monto_pagado = models.IntegerField(default=0)
    intereses = models.DecimalField(decimal_places=2, max_digits=3)
    fecha_inicio_cuotas = models.CharField(max_length=50)
    fecha_fin_cuotas = models.CharField(max_length=50)
    estado_pago = models.CharField(max_length=50)
    monto_restante = models.IntegerField(default=0)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cedula_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cedula_cliente
        
    class Meta:
        db_table = 'Credito'