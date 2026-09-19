from django.urls import path
from apps.administration.views import AdminUserDetailView, AdminUserListView, AdminUserToggleStatusView

urlpatterns = [
    path('', AdminUserListView.as_view(), name='user-list'),
    path('<int:user_id>/', AdminUserDetailView.as_view(), name='user-detail'),
    path('<int:user_id>/toggle-status/', AdminUserToggleStatusView.as_view(), name='user-toggle-status'),
]