from rest_framework import serializers
from apps.administration.models import SocietyInfo


class SocietyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyInfo
        fields = [
            'id',
            'name',
            'registration_no',
            'address',
            'city',
            'state',
            'pin_code',
            'phone',
            'email',
            'created_at',
            'updated_at',
        ]