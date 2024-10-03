from rest_framework.routers import DefaultRouter

from .views import ConsultasViewSet, PacientesViewSet, CitasViewSet, MedicosViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultasViewSet, basename='consultas')
router.register(r'citas', CitasViewSet, basename='citas')
router.register(r'pacientes', PacientesViewSet, basename='pacientes')
router.register(r'medicos', MedicosViewSet, basename='medicos')


urlpatterns = router.urls