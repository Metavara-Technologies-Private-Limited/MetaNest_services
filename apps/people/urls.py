from rest_framework.routers import DefaultRouter

from .views import ResidentViewSet, SecurityStaffViewSet


router = DefaultRouter()
router.register(r"security-staff", SecurityStaffViewSet, basename="security-staff")
router.register(r"residents", ResidentViewSet, basename="resident")

urlpatterns = router.urls
