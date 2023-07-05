from rest_framework import routers
from . import api

# Routers provee una forma simple de direccionar las peticiones a diferentes vistas basadas en el método de la petición (GET, POST, PUT, DELETE).
router = routers.DefaultRouter()

#Se registran las vistas de la app
router.register(r'rol', api.RolViewSet, basename='admin_rol')
router.register(r'sucursal', api.SucursalViewSet, basename='admin_sucursal')
router.register(r'estado', api.EstadoViewSet, basename='admin_estado')
router.register(r'usuario', api.UsuarioViewSet, basename='admin_usuario')
router.register(r'proveedor', api.ProveedorViewSet, basename='admin_proveedor')
router.register(r'auto', api.AutoViewSet, basename='admin_auto')
router.register(r'cita', api.CitaViewSet, basename='admin_cita')
router.register(r'venta',api.VentaViewSet, basename='admin_venta')
router.register(r'pago', api.PagoViewSet, basename='admin_pago')
router.register(r'registaller', api.RegistroTallerViewSet, basename='admin_registaller')
router.register(r'repuesto', api.RepuestoViewSet, basename='admin_repuesto')
router.register(r'credito', api.CreditoViewSet, basename='admin_credito')
router.register(r'reporte', api.ReporteViewSet, basename='admin_reporte')
router.register(r'queja', api.QuejaViewSet, basename='admin_queja')

#Se asignan las urls de la app
urlpatterns = router.urls