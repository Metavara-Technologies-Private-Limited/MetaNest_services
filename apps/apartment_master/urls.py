from rest_framework.routers import DefaultRouter

from apps.apartment_master.views import (
    FlatTypeViewSet,
    FlatViewSet,
    FloorViewSet,
    SocietyViewSet,
    WingViewSet,
)

router = DefaultRouter()
router.register(r"societies", SocietyViewSet, basename="society")
router.register(r"wings", WingViewSet, basename="wing")
router.register(r"floors", FloorViewSet, basename="floor")
router.register(r"flat-types", FlatTypeViewSet, basename="flat-type")
router.register(r"flats", FlatViewSet, basename="flat")

urlpatterns = router.urls