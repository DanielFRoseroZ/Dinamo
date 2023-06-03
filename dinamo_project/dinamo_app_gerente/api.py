from . import models
from rest_framework import viewsets, permissions
from . import serializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = models.Rol.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.RolSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = models.Sucursal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.SucursalSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.UsuarioSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = models.Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.ProveedorSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = models.Auto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.AutoSerializer

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