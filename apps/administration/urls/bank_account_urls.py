from django.urls import path
from apps.administration.views import BankAccountView

urlpatterns = [
    path('', BankAccountView.as_view(), name='bank-account-setting'),
]