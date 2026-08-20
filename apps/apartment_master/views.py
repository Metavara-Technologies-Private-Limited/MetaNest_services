# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.apartment_master import services
from apps.apartment_master.models import Flat, FlatType, Floor, Society, Wing
from apps.apartment_master.serializers import (
    FlatSerializer,
    FlatTypeSerializer,
    FloorSerializer,
    SocietySerializer,
    SocietySummarySerializer,
    WingSerializer,
)


class SocietyViewSet(viewsets.ModelViewSet):
    """
    Views stay thin: no querysets with business logic, no calculations.
    Everything beyond basic CRUD is delegated to services.py.
    """

    queryset = Society.objects.prefetch_related("wings").all()
    serializer_class = SocietySerializer
    permission_classes = [IsAuthenticated]
    ordering = ["name"]

    @action(detail=True, methods=["get"], url_path="summary")
    def summary(self, request, pk=None):
        society = self.get_object()
        data = services.get_society_summary(society)
        serializer = SocietySummarySerializer(data)
        return Response(serializer.data)


class WingViewSet(viewsets.ModelViewSet):
    queryset = Wing.objects.select_related("society").all()
    serializer_class = WingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        society_id = self.request.query_params.get("society")
        if society_id:
            qs = qs.filter(society_id=society_id)
        return qs.order_by("name")


class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.select_related("wing").all()
    serializer_class = FloorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        wing_id = self.request.query_params.get("wing")
        if wing_id:
            qs = qs.filter(wing_id=wing_id)

        return qs.order_by("floor_number")


class FlatTypeViewSet(viewsets.ModelViewSet):
    queryset = FlatType.objects.all()
    serializer_class = FlatTypeSerializer
    permission_classes = [IsAuthenticated]


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.select_related("floor", "floor__wing", "flat_type").all()
    serializer_class = FlatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        floor_id = self.request.query_params.get("floor")
        wing_id = self.request.query_params.get("wing")
        flat_type_id = self.request.query_params.get("flat_type")
        if floor_id:
            qs = qs.filter(floor_id=floor_id)
        if wing_id:
            qs = qs.filter(floor__wing_id=wing_id)
        if flat_type_id:
            qs = qs.filter(flat_type_id=flat_type_id)
        return qs.order_by("flat_number")