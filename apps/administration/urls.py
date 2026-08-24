from django.urls import path

from .views import AdminUserListView, AdminUserToggleStatusView


urlpatterns = [
	path("", AdminUserListView.as_view(), name="admin-user-list"),
	path("<int:user_id>/toggle-status/", AdminUserToggleStatusView.as_view(), name="admin-user-toggle-status"),
]
