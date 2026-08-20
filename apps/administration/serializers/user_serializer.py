from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'mobile_number',
            'first_name',
            'last_name',
            'role',
            'is_active',
            'is_superuser',
            'last_login',
        ]
        read_only_fields = ['id']