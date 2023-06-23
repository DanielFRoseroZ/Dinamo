from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('rol', views.RolViewSet, 'admin_rol')
router.register('sucursal', views.SucursalViewSet, 'admin_sucursal')
router.register('estado', views.EstadoViewSet, 'admin_estado')
router.register('usuario', views.UsuarioViewSet, 'admin_usuario')
router.register('proveedor', views.ProveedorViewSet, 'admin_proveedor')
router.register('auto', views.AutoViewSet, 'admin_auto')
router.register('cita', views.CitaViewSet, 'admin_cita')
router.register('venta',views.VentaViewSet, 'admin_venta')
router.register('pago', views.PagoViewSet, 'admin_pago')
router.register('registaller', views.RegistroTallerViewSet, 'admin_registaller')
router.register('repuesto', views.RepuestoViewSet, 'admin_repuesto')
router.register('credito', views.CreditoViewSet, 'admin_credito')
router.register('reporte', views.ReporteViewSet, 'admin_reporte')

urlpatterns = router.urls