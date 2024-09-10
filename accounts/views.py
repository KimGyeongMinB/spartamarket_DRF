from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User # 모델에 있는 USER 가져오기
from .validators import validate_signup

# Create your views here.
# 회원가입
class SignupAPIView(APIView):
    def post(self, request):
        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=400)

        User.objects.create_user(
            username=request.data.get("username"),
            password=request.data.get("password"),
            nickname=request.data.get("nickname"),
            birthday=request.data.get("birthday"),
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name"),
            email=request.data.get("email"),
            # introduce = request.data.get("introduce")
            gender=request.data.get("gender"),
        )

        return Response({'message': '회원가입이 완료되었습니다'}, status=200)