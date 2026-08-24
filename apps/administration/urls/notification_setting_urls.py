from django.urls import path
from apps.administration.views import NotificationSettingView

urlpatterns = [
    path('', NotificationSettingView.as_view(), name='notification-setting'),
]