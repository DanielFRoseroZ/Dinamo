from rest_framework import routers
from . import api

router = routers.DefaultRouter()

router.register('admin/rol', api.RolViewSet, 'admin_rol')
router.register('admin/sucursal', api.SucursalViewSet, 'admin_sucursal')
router.register('admin/estado', api.EstadoViewSet, 'admin_estado')
router.register('admin/usuario', api.UsuarioViewSet, 'admin_usuario')
router.register('admin/proveedor', api.ProveedorViewSet, 'admin_proveedor')
router.register('admin/auto', api.AutoViewSet, 'admin_auto')
router.register('admin/cita', api.CitaViewSet, 'admin_cita')
router.register('admin/venta',api.VentaViewSet, 'admin_venta')
router.register('admin/pago', api.PagoViewSet, 'admin_pago')
router.register('admin/registaller', api.RegistroTallerViewSet, 'admin_registaller')
router.register('admin/repuesto', api.RepuestoViewSet, 'admin_repuesto')
router.register('admin/credito', api.CreditoViewSet, 'admin_credito')
router.register('admin/reporte', api.ReporteViewSet, 'admin_reporte')

urlpatterns = router.urls