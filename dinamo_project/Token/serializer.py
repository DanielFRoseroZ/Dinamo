from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from dinamo_app_gerente import models, serializer

#Configuración de la serialización del token, para que valores adicionales se puede agregar con un query -> Se serializa el dato -> Se agrega al token
class Serializador_token(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #Query para obtener el username del usuario
        query = models.Usuario.objects.get(username=user.username)
        usuario = serializer.UsuarioSerializer(query)

        #Query para obtener el rol del usuario
        query_rol = models.Rol.objects.get(id=usuario.data['rol'])
        rol = serializer.RolSerializer(query_rol)

        #Query para obtener el nombre del usuario
        query_name = models.Usuario.objects.get(nombre=usuario.data['nombre'])
        nombre = serializer.UsuarioSerializer(query_name)

        #Se agrega el rol y nombre al token
        token['role'] = rol.data['nombre']
        token[ 'name'] = nombre.data['nombre']
        return token