from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class AdminUserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='mobile_number', write_only=True, required=True)
    email = serializers.EmailField(required=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'phone_number',
            'first_name',
            'last_name',
            'email',
            'role',
            'is_active',
            'is_superuser',
            'last_login',
            'status',
        ]
        read_only_fields = ['id']

    def get_status(self, obj):
        return 'Active' if obj.is_active else 'Inactive'

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError('Enter a valid 10-digit mobile number.')
        return value

    def validate(self, attrs):
        mobile_number = attrs.get('mobile_number')
        if User.objects.filter(mobile_number=mobile_number).exists():
            raise serializers.ValidationError({'phone_number': 'A user with this phone number already exists.'})
        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError({'email': 'A user with this email already exists.'})
        return attrs

    def create(self, validated_data):
        mobile_number = validated_data.pop('mobile_number')
        return User.objects.create_user(mobile_number=mobile_number, **validated_data)