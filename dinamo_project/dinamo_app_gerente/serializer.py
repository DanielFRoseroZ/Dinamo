from rest_framework import serializers
from . import models

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Usuario
        fields = '__all__'
        
class Rol_serializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Rol
        fields = '__all__'
        
class Sucursal_serializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Sucursal
        fields = '__all__'