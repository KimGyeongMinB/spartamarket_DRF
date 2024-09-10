from . import views
from django.urls import path

app_name = 'products'

urlpatterns = [
    path("products/", views.GoodsAPIView.as_view(), name="goods"),
    path("products/<int:productId>/", views.GoodsAPIView.as_view(), name="goods"),
]