from rest_framework import serializers
from . import models

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rol
        fields = ('id', 'nombre',)
        read_only_fields = ('id',)
    
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sucursal
        fields = ('id', 'nombre', 'direccion', 'telefono', 'correo',)
        read_only_fields = ('id',)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Proveedor
        fields = '__all__'

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Auto
        fields = '__all__'

class RepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Repuesto
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cita
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venta
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pago
        fields = '__all__'
    
class RegistroTallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RegistroTaller
        fields = '__all__'

class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Credito
        fields = '__all__'