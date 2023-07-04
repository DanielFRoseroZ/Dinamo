from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from . import models
from django.contrib.auth.models import User

#Configuración de los serializadores para los datos de la base de datos -> Se serializan los datos para que se puedan enviar en formato JSON

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rol
        fields = '__all__'
    
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sucursal
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estado
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    #Se crea el usuario con el username y el password en la tabla de user de django, para poder utilizar el login y autenticación de django
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        validated_data['password'] = make_password(validated_data['password'])
        user.password = validated_data['password'] 
        user.save()
        return super().create(validated_data)

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

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reporte
        fields = '__all__'

class QuejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Queja
        fields = '__all__'