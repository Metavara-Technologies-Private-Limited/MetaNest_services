from django.urls import path
from apps.administration.views import AdminUserListView, AdminUserToggleStatusView

urlpatterns = [
    path('', AdminUserListView.as_view(), name='user-list'),
    path('<int:user_id>/toggle-status/', AdminUserToggleStatusView.as_view(), name='user-toggle-status'),
]