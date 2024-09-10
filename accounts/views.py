from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User # 모델에 있는 USER 가져오기
from .validators import validate_signup, validate_update_user
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate # 로그인
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

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
    
# 로그인
class SigninAPIView(APIView):
    permission_classes = [AllowAny] # 로그인 인증 미진행 

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        # 사용자가 None 이 아닐경우 진행
        if user is not None:
            serializer = UserSerializer(user)
            res_data = serializer.data

            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            res_data["access_token"] = access_token
            res_data["refresh_token"] = refresh_token

            return Response({"message": "로그인성공하셨습니다", "data": res_data}, status=200)
        return Response({"message": "로그인에 실패하셨습니다. 다시해주세요"}, status=400)
    
# 로그아웃
class LogoutAPIView(APIView):
	# login한 user에 대한 확인 필요.
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token_str = request.data.get("refresh_token")
        refresh_token = RefreshToken(refresh_token_str)
        refresh_token.blacklist()

        return Response({"로그아웃 완료되었습니다"}, status=200)
    

class Profiledetail(APIView):
# 로그인 했을 때 적용
    permission_classes = [IsAuthenticated]

# 유저 정보 불러오기
    def get(self, request, username):
        user_profile = get_object_or_404(User, username=username)
        serializer = UserSerializer(user_profile)
        return Response(serializer.data)
    
# 유저 정보 수정
    def put(self, request, username):
        user = User.objects.get(username=username)

        is_valid, err_msg = validate_update_user(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=400)

        nickname = request.data.get("nickname")
        username = request.data.get("username")
        email = request.data.get("email")
        birthday = request.data.get("birthday")

        user.nickname = nickname
        user.username = username
        user.email = email
        user.birthday = birthday

        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)