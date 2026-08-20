from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.administration.serializers import SocietyInfoSerializer
from apps.administration.services import SocietyInfoService


class SocietyInfoView(APIView):
    permission_classes = [AllowAny]  # <-- Allows access without token

    def get(self, request):
        info = SocietyInfoService.get_society_info()
        serializer = SocietyInfoSerializer(info)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        info = SocietyInfoService.update_society_info(request.data)
        serializer = SocietyInfoSerializer(info)
        return Response(serializer.data, status=status.HTTP_200_OK)