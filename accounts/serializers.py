from rest_framework import serializers
from .models import User  # User 모델 임포트

# 로그인 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # 사용하는 모델 지정
        fields = ['username','gender', 'nickname', 'birthday', 'email']


# 비밀번호 변경 시리얼라이저
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)