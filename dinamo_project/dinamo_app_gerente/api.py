from . import models
from django.db.models import Q
from rest_framework import viewsets, permissions
from . import serializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = models.Rol.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.RolSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')

        if search_term:
            queryset = queryset.filter(
                Q(nombre__icontains=search_term)
            )
        return queryset

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = models.Sucursal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.SucursalSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(nombre__icontains=search_term)
            )
        return queryset

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = models.Estado.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.EstadoSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(nombre__icontains=search_term)
            )
        return queryset

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.UsuarioSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(cedula__icontains=search_term) |
                Q(nombre__icontains=search_term) |
                Q(correo__icontains=search_term) |
                Q(telefono__icontains=search_term) |
                Q(direccion__icontains=search_term) |
                Q(sucursal__nombre__icontains=search_term) |
                Q(rol__nombre__icontains=search_term)
            )
        return queryset

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = models.Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.ProveedorSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(nombre__icontains=search_term) |
                Q(nombre__producto__icontains=search_term)
            )
        return queryset

class AutoViewSet(viewsets.ModelViewSet):
    queryset = models.Auto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.AutoSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(modelo__icontains=search_term) |
                Q(año__icontains=search_term) |
                Q(color__icontains=search_term) |
                Q(precio_icontains=search_term)
            )
        return queryset

class RepuestoViewSet(viewsets.ModelViewSet):
    queryset = models.Repuesto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.RepuestoSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = models.Cita.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.CitaSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = models.Venta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.VentaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = models.Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.PagoSerializer

class RegistroTallerViewSet(viewsets.ModelViewSet):
    queryset = models.RegistroTaller.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.RegistroTallerSerializer

class CreditoViewSet(viewsets.ModelViewSet):
    queryset = models.Credito.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.CreditoSerializer