from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.administration.serializers import AdminUserSerializer
from apps.administration.services import AdminUserService


class AdminUserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = AdminUserService.get_all_users()
        serializer = AdminUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AdminUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(AdminUserSerializer(user).data, status=status.HTTP_201_CREATED)


class AdminUserToggleStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user = AdminUserService.toggle_user_status(user_id)
        if user:
            serializer = AdminUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )