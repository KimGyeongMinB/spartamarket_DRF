from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("accounts/", views.SignupAPIView.as_view(), name="signup"),
]