from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.analytics.serializers.analytics_serializer import (
    CollectionReportSerializer,
    OccupancyReportSerializer,
    OutstandingReportSerializer,
)
from apps.analytics.services.analytics_service import (
    get_collection_report,
    get_occupancy_report,
    get_outstanding_report,
)


class CollectionReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_collection_report()

        serializer = CollectionReportSerializer(
            instance=data,
        )

        return Response(serializer.data)


class OutstandingReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_outstanding_report()

        serializer = OutstandingReportSerializer(
            instance=data,
        )

        return Response(serializer.data)


class OccupancyReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_occupancy_report()

        serializer = OccupancyReportSerializer(
            instance=data,
        )

        return Response(serializer.data)
