from apps.administration.models import SystemNotification


class NotificationService:
    @staticmethod
    def get_all_notifications():
        return SystemNotification.objects.all()

    @staticmethod
    def get_unread_count():
        return SystemNotification.objects.filter(is_read=False).count()

    @staticmethod
    def mark_all_as_read():
        return SystemNotification.objects.filter(is_read=False).update(is_read=True)

    @staticmethod
    def create_notification(title, message, notification_type):
        return SystemNotification.objects.create(
            title=title,
            message=message,
            notification_type=notification_type,
            is_read=False
        )