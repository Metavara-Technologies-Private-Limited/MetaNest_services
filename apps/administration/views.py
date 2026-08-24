from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.authentication.models import User
from .serializers import AdminUserSerializer


class IsAdmin(IsAuthenticated):
	def has_permission(self, request, view):
		return super().has_permission(request, view) and request.user.role == "ADMIN"


class AdminUserListView(APIView):
	permission_classes = [IsAdmin]

	def get(self, request):
		users = User.objects.filter(is_active=True).order_by("-created_at")
		return Response(AdminUserSerializer(users, many=True).data)

	def post(self, request):
		serializer = AdminUserSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response(AdminUserSerializer(user).data, status=status.HTTP_201_CREATED)


class AdminUserToggleStatusView(APIView):
	permission_classes = [IsAdmin]

	def patch(self, request, user_id):
		user = User.objects.get(pk=user_id)
		user.is_active = not user.is_active
		user.save(update_fields=["is_active", "updated_at"])
		return Response(AdminUserSerializer(user).data)

# Create your views here.
