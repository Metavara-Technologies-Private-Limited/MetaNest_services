from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.administration.serializers import BankAccountSerializer
from apps.administration.services import BankAccountService


class BankAccountView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        account = BankAccountService.get_primary_bank_account()
        serializer = BankAccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        account = BankAccountService.update_bank_account(request.data)
        serializer = BankAccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)