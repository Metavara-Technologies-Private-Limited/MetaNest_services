from django.db import models


class NotificationSetting(models.Model):
    sms_notifications = models.BooleanField(default=True)
    email_notifications = models.BooleanField(default=True)
    whatsapp_notifications = models.BooleanField(default=False)
    payment_reminders = models.BooleanField(default=True)
    overdue_alerts = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Notification Preferences"