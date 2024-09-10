from rest_framework import serializers
from .models import Goods  # 모델을 임포트하는 부분을 추가합니다.

class GoodsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Goods
        fields = ['id','title', 'content', 'price', 'created_at', 'updated_at', 'image']