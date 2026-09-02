from django.urls import path

from apps.analytics.views.analytics_view import (
    CollectionReportView,
    OutstandingReportView,
    OccupancyReportView,
)


urlpatterns = [
    path(
        "collection/",
        CollectionReportView.as_view(),
        name="analytics-collection",
    ),
    path(
        "outstanding/",
        OutstandingReportView.as_view(),
        name="analytics-outstanding",
    ),
    path(
        "occupancy/",
        OccupancyReportView.as_view(),
        name="analytics-occupancy",
    ),
]
