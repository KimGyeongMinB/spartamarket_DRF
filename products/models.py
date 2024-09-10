from django.conf import settings
from django.db import models
from accounts.models import User

# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=100) # 제목
    content = models.TextField(blank=True) # 내용
    price = models.DecimalField(max_digits=10, decimal_places=2) # 가격
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일 
    updated_at = models.DateTimeField(auto_now=True)  # 수정일 
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    image = models.ImageField(upload_to="images/", blank=True, null=True)