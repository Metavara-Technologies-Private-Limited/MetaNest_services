from apps.administration.models import NotificationSetting


class NotificationSettingService:
    @staticmethod
    def get_notification_settings():
        obj, _ = NotificationSetting.objects.get_or_create(
            id=1,
            defaults={
                "sms_notifications": True,
                "email_notifications": True,
                "whatsapp_notifications": False,
                "payment_reminders": True,
                "overdue_alerts": True,
            }
        )
        return obj

    @staticmethod
    def update_notification_settings(data):
        obj = NotificationSettingService.get_notification_settings()
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        return obj