from django.urls import path
from apps.administration.views import RoleListView

urlpatterns = [
    path('', RoleListView.as_view(), name='role-list'),
]