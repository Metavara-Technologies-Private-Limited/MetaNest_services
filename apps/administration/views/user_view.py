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


class AdminUserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, user_id):
        user = AdminUserService.get_user_by_id(user_id)
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdminUserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(AdminUserSerializer(serializer.save()).data, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        user = AdminUserService.get_user_by_id(user_id)
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        if user.id == request.user.id:
            return Response({"error": "You cannot delete the account currently signed in."}, status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminUserToggleStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, user_id):
        user = AdminUserService.toggle_user_status(user_id)
        if user:
            serializer = AdminUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )