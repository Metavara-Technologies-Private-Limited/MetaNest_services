from django.db import models


class SystemNotification(models.Model):
    class NotificationType(models.TextChoices):
        PAYMENT_RECEIVED = 'PAYMENT_RECEIVED', 'Payment Received'
        OVERDUE_ALERT = 'OVERDUE_ALERT', 'Overdue Alert'
        SOCIETY_AGM = 'SOCIETY_AGM', 'Society AGM'
        BILLS_GENERATED = 'BILLS_GENERATED', 'Bills Generated'

    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_type = models.CharField(max_length=30, choices=NotificationType.choices)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title}: {self.message[:30]}"