from django.urls import path
from apps.administration.views import BillingSettingView

urlpatterns = [
    path('', BillingSettingView.as_view(), name='billing-setting'),
]