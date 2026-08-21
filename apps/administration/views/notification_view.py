from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.administration.serializers import NotificationSerializer
from apps.administration.services import NotificationService


class NotificationListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        notifications = NotificationService.get_all_notifications()
        unread_count = NotificationService.get_unread_count()
        serializer = NotificationSerializer(notifications, many=True)
        return Response({
            "unread_count": unread_count,
            "results": serializer.data
        }, status=status.HTTP_200_OK)


class NotificationMarkAllReadView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        NotificationService.mark_all_as_read()
        return Response({"message": "All notifications marked as read."}, status=status.HTTP_200_OK)