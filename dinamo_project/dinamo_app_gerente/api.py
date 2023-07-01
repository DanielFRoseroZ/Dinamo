from . import models
from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from . import serializer
import cloudinary.uploader
from django.contrib.auth import authenticate, login
from rest_framework.decorators import action
from .models import Usuario

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
    
    @action(detail=False, methods=['POST'], url_path='login_xd')
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        
        if user != None:
            login(request, user)
            return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
    
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
                Q(tipo_producto__incontains=search_term) |
                Q(nombre_producto__icontains=search_term)
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
                Q(precio__icontains=search_term)
            )
        return queryset

class RepuestoViewSet(viewsets.ModelViewSet):
    queryset = models.Repuesto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.RepuestoSerializer
    
    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(articulo__icontains=search_term) |
                Q(sucursal__nombre__icontains=search_term) |
                Q(proveedor__nombre__icontains=search_term)
            )
        return queryset


class CitaViewSet(viewsets.ModelViewSet):
    queryset = models.Cita.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.CitaSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(fecha__icontains=search_term) |
                Q(nombre_empleado__icontains=search_term) |
                Q(nombre_cliente__icontains=search_term)
            )
        return queryset

class VentaViewSet(viewsets.ModelViewSet):
    queryset = models.Venta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.VentaSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(nombre_vendedor__icontains=search_term) |
                Q(fecha_venta__icontains=search_term)
            )
        return queryset

class PagoViewSet(viewsets.ModelViewSet):
    queryset = models.Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.PagoSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(cantidad_pago__icontains=search_term) |
                Q(nombre_cliente__icontains=search_term) |
                Q(id_venta__id__icontains=search_term)
            )
        return queryset

class RegistroTallerViewSet(viewsets.ModelViewSet):
    queryset = models.RegistroTaller.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.RegistroTallerSerializer

        #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(placa_auto__icontains=search_term) |
                Q(estado__icontains=search_term) |
                Q(fecha_ingreso__icontains=search_term)
            )
        return queryset

class CreditoViewSet(viewsets.ModelViewSet):
    queryset = models.Credito.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializer.CreditoSerializer

    #Funcion que recibe los parametros de una busqueda a traves de la URL y realiza la peticion correspondiente a la BD, para filtrar los datos y mostrarlos en pantalla 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(monto_pagado__icontains=search_term) |
                Q(estado_pago__icontains=search_term) |
                Q(cedula_cliente__nombre__icontains=search_term)
            )
        return queryset
    
class ReporteViewSet(viewsets.ModelViewSet):
    queryset = models.Reporte.objects.all()
    serializer_class = serializer.ReporteSerializer

    def pdf_create(self, serializer):
        archivo_pdf = self.request.get['archivo_pdf']
        upload_result = cloudinary.uploader.upload(archivo_pdf)
        serializer.save(archivo_pdf=upload_result['url'])
        
    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        
        if search_term:
            queryset = queryset.filter(
                Q(titulo__icontains=search_term) |
                Q(rol__nombre__icontains=search_term)
            )
        return queryset