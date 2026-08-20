from rest_framework import serializers
from apps.administration.models import SystemNotification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemNotification
        fields = [
            'id',
            'title',
            'message',
            'notification_type',
            'is_read',
            'created_at',
        ]