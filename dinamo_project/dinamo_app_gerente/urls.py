from rest_framework import routers
from . import api

router = routers.DefaultRouter()

router.register('rol', api.RolViewSet, 'admin_rol')
router.register('sucursal', api.SucursalViewSet, 'admin_sucursal')
router.register('estado', api.EstadoViewSet, 'admin_estado')
router.register('usuario', api.UsuarioViewSet, 'admin_usuario')
router.register('proveedor', api.ProveedorViewSet, 'admin_proveedor')
router.register('auto', api.AutoViewSet, 'admin_auto')
router.register('cita', api.CitaViewSet, 'admin_cita')
router.register('venta',api.VentaViewSet, 'admin_venta')
router.register('pago', api.PagoViewSet, 'admin_pago')
router.register('registaller', api.RegistroTallerViewSet, 'admin_registaller')
router.register('repuesto', api.RepuestoViewSet, 'admin_repuesto')
router.register('credito', api.CreditoViewSet, 'admin_credito')
router.register('reporte', api.ReporteViewSet, 'admin_reporte')

urlpatterns = router.urls