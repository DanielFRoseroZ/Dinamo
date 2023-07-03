from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Auto)
admin.site.register(models.Reporte)
admin.site.register(models.Usuario)
admin.site.register(models.Sucursal)
admin.site.register(models.Estado)
admin.site.register(models.Proveedor)
admin.site.register(models.Cita)
admin.site.register(models.Venta)
admin.site.register(models.Pago)
admin.site.register(models.RegistroTaller)
admin.site.register(models.Repuesto)
admin.site.register(models.Credito)
admin.site.register(models.Rol)