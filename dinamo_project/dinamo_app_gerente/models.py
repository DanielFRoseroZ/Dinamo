from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from .validators import validate_file_extension, validate_numeric, validate_email, validate_str, validate_file_extension_imgs, validate_fecha_format

# Create your models here.

#Modelo de la tabla Rol
class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True, validators=[validate_str])
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Rol' 
    
#Modelo de la tabla Sucursal
class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50, validators=[validate_numeric])
    correo = models.CharField(max_length=200, validators=[validate_email])
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Sucursal'
        
#Modelo de la tabla Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validate_str])
    telefono = models.CharField(max_length=50, validators=[validate_numeric])
    correo = models.CharField(max_length=100, validators=[validate_email])
    tipo_producto = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Proveedor'    

class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Estado'

#Modelo de la tabla Usuario
class Usuario(models.Model):
    cedula = models.CharField('Cédula', primary_key=True, max_length=50, validators=[validate_numeric])
    nombre = models.CharField(max_length=200, validators=[validate_str])
    username = models.CharField('Correo Eléctronico', max_length=200, unique=True, validators=[validate_email])
    telefono = models.CharField('Teléfono', max_length=200, validators=[validate_numeric])
    direccion = models.CharField('Dirección', max_length=200)
    password = models.CharField('Contraseña', max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cedula
    
    class Meta:
        db_table = 'Usuario'

#Modelo de la tabla Cliente
class Auto(models.Model):
    modelo = models.CharField(max_length=200)
    color = models.CharField(max_length=50, validators=[validate_str])
    foto = models.FileField(upload_to='fotos_autos', validators=[validate_file_extension_imgs])
    precio = models.IntegerField(default=0)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    año = models.CharField(max_length=10, validators=[validate_numeric])
    caracteristicas = models.CharField(max_length=300)
    kilometraje = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.modelo
    
    class Meta:
        db_table = 'Auto'

#Modelo de la tabla Repuesto
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

#Modelo de la tabla Cita
class Cita(models.Model):
    fecha = models.CharField(max_length=10, validators=[validate_fecha_format])
    nombre_empleado = models.CharField(max_length=100, validators=[validate_str])
    cedula_empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cedula_empleado')
    nombre_cliente = models.CharField(max_length=100, validators=[validate_str])
    cedula_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cedula_cliente')
    descripcion = models.CharField(max_length=400)
    
    def __str__(self):
        return self.fecha
    
    class Meta:
        db_table = 'Cita'
    
#Modelo de la tabla Venta
class Venta(models.Model):
    precio = models.IntegerField(default=0)
    nombre_vendedor = models.CharField(max_length=100, validators=[validate_str])
    cedula_vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_venta = models.CharField(max_length=100, validators=[validate_fecha_format])
    comentario = models.CharField(max_length=200)
    metodo_pago = models.CharField(max_length=50, validators=[validate_str])
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_vendedor
        
    class Meta:
        db_table = 'Venta'    

#Modelo de la tabla Pago
class Pago(models.Model):
    tipo_pago = models.CharField(max_length=100, validators=[validate_str])
    cantidad_pago = models.IntegerField(default=0)
    nombre_cliente = models.CharField(max_length=200, validators=[validate_str])
    cedula_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    meotodo_pago = models.CharField(max_length=100, validators=[validate_str])
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_cliente
    
    class Meta:
        db_table = 'Pago'

#Modelo de la tabla RegistroTaller
class RegistroTaller(models.Model):
    placa_auto = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, validators=[validate_str])
    comentario = models.CharField(max_length=200,)
    fecha_ingreso = models.CharField(max_length=100, validators=[validate_fecha_format])
    fecha_entregado = models.CharField(max_length=100, validators=[validate_fecha_format])
    costo_reparacion = models.IntegerField(default=0)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    mecanico_encargado = models.CharField(max_length=100, validators=[validate_str])
    cedula_mecanico = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.modelo
        
    class Meta:
        db_table = 'RegistroTaller'

#Modelo de la tabla Credito
class Credito(models.Model):
    monto_pagado = models.IntegerField(default=0)
    intereses = models.DecimalField(decimal_places=2, max_digits=3)
    fecha_inicio_cuotas = models.CharField(max_length=10, validators=[validate_fecha_format])
    fecha_fin_cuotas = models.CharField(max_length=10, validators=[validate_fecha_format])
    estado_pago = models.CharField(max_length=50, validators=[validate_str])
    monto_restante = models.IntegerField(default=0)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cliente
        
    class Meta:
        db_table = 'Credito'

#Modelo de la tabla Reporte
class Reporte(models.Model):
    titulo = models.CharField(max_length=200, default='Reporte')
    archivo_pdf = models.FileField(upload_to='reportes', validators=[validate_file_extension])
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.archivo_pdf
    
    class Meta:
        db_table = 'Reporte'

#Modelo de la tabla Quejas 
class Queja(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto
    
    class Meta:
        db_table = 'Quejas' 

#Modelo de la tabla AutoTaller - para registrar los autos que ingresan al taller por reparacion
class AutoTaller(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveBigIntegerField(default=0)
    placa = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_ingreso = models.CharField(max_length=10, validators=[validate_fecha_format])

    def __str__(self):
        return self.placa
    
    class Meta:
        db_table = 'AutoTaller'

#Modelo de la tabla Cotizacion - para registrar la cotizacion inicial realizada a un auto ingresado por reparacion
class Cotizacion(models.Model):
    fecha = models.CharField(max_length=10, validators=[validate_fecha_format])
    descripcion = models.TextField()
    costo_cotizacion = models.DecimalField(max_digits=10, decimal_places=2)
    auto = models.ForeignKey(AutoTaller, on_delete=models.CASCADE)

    def __str__(self):
        return f'Auto: {self.auto}'
    
    class Meta:
        db_table = 'Cotizacion'

#Modelo de la tabla OrdenTrabajo - para registrar las ordenes de trabajo asociadas a los autos ingresados para reparacion
class OrdenTrabajo(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en proceso', 'En proceso'),
        ('finalizado', 'Finalizado'),
    )

    auto = models.ForeignKey(AutoTaller, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=10, validators=[validate_fecha_format])
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE,default= None)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    descripcion = models.TextField()
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.auto

    class Meta:
        db_table = 'OrdenTrabajo'