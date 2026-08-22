from django.urls import path

from apps.finance.views import (
    MaintenanceConfigurationView,
    BillView,
    PaymentView,
    LateFeeView,
    LateFeeHistoryView,
    WaiveLateFeeView,
)


urlpatterns = [
    path(
        "maintenance-configuration/",
        MaintenanceConfigurationView.as_view(),
        name="maintenance-configuration"
    ),

    path(
        "bills/",
        BillView.as_view(),
        name="bill-create",
    ),
    path(
        "payments/",
        PaymentView.as_view(),
        name="payment-create",
    ),

    path(
        "late-fees/",
        LateFeeView.as_view(),
        name="late-fee-create",
    ),

    path(
        "late-fee-history/",
        LateFeeHistoryView.as_view(),
        name="late-fee-history",
    ),

    path(
        "late-fees/waive/",
        WaiveLateFeeView.as_view(),
        name="late-fee-waive",
    ),
]