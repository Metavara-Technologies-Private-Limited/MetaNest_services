from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Resident, SecurityStaff
from .serializers import ResidentSerializer, SecurityStaffSerializer


class SecurityStaffViewSet(viewsets.ModelViewSet):
	queryset = SecurityStaff.objects.all().order_by("-created_at")
	serializer_class = SecurityStaffSerializer
	permission_classes = [IsAuthenticated]


class ResidentViewSet(viewsets.ModelViewSet):
	queryset = Resident.objects.select_related("flat").all().order_by("-created_at")
	serializer_class = ResidentSerializer
	permission_classes = [IsAuthenticated]
