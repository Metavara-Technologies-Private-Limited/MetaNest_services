from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.administration.serializers import AdminUserSerializer
from apps.administration.services import AdminUserService


class AdminUserListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = AdminUserService.get_all_users()
        serializer = AdminUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminUserToggleStatusView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, user_id):
        user = AdminUserService.toggle_user_status(user_id)
        if user:
            serializer = AdminUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )