from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.administration.serializers import NotificationSettingSerializer
from apps.administration.services import NotificationSettingService


class NotificationSettingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        settings = NotificationSettingService.get_notification_settings()
        serializer = NotificationSettingSerializer(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        settings = NotificationSettingService.update_notification_settings(request.data)
        serializer = NotificationSettingSerializer(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)