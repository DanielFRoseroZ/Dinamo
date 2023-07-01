from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from dinamo_app_gerente import models, serializer

class Serializador_token(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        query = models.Usuario.objects.get(username=user.username)
        usuario = serializer.UsuarioSerializer(query)
        query_rol = models.Rol.objects.get(id=usuario.data['rol'])
        rol = serializer.RolSerializer(query_rol)
        token['role'] = rol.data['nombre']
        return token