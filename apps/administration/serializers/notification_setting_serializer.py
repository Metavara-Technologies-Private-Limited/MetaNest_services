from rest_framework import serializers
from apps.administration.models import NotificationSetting


class NotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSetting
        fields = [
            'id',
            'sms_notifications',
            'email_notifications',
            'whatsapp_notifications',
            'payment_reminders',
            'overdue_alerts',
            'created_at',
            'updated_at',
        ]