from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.administration.serializers import BillingSettingSerializer
from apps.administration.services import BillingSettingService


class BillingSettingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        setting = BillingSettingService.get_billing_settings()
        serializer = BillingSettingSerializer(setting)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        setting = BillingSettingService.update_billing_settings(request.data)
        serializer = BillingSettingSerializer(setting)
        return Response(serializer.data, status=status.HTTP_200_OK)