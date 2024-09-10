from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("accounts/", views.SignupAPIView.as_view(), name="signup"),
    path("accounts/logout/", views.LogoutAPIView.as_view(), name="logout"),
    path("accounts/signin/", views.SigninAPIView.as_view(), name="signin"),
    path("accounts/<str:username>/", views.Profiledetail.as_view(), name="profile"),
    
]