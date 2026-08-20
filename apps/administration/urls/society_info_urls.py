from django.urls import path
from apps.administration.views import SocietyInfoView

urlpatterns = [
    path('', SocietyInfoView.as_view(), name='society-info'),
]