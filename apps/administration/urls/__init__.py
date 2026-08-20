from django.urls import path, include

urlpatterns = [
    path('society/', include('apps.administration.urls.society_info_urls')),
    path('bank-account/', include('apps.administration.urls.bank_account_urls')),
    path('billing/', include('apps.administration.urls.billing_setting_urls')),
    path('notification-settings/', include('apps.administration.urls.notification_setting_urls')),
    path('notifications/', include('apps.administration.urls.notification_urls')),
    path('roles/', include('apps.administration.urls.role_urls')),
    path('users/', include('apps.administration.urls.user_urls')),
]