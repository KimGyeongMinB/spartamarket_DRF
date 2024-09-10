from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import GoodsSerializer
from rest_framework.response import Response
from .models import Goods
from accounts.models import User
from django.core.paginator import Paginator

# from rest_framework.permissions import IsAuthenticated
# Create your views here.

class GoodsAPIView(APIView):
    # 상품 등록
    def post(self, request):
        if request.user.is_authenticated: # 로그인 상태일때
            serializer = GoodsSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"message":"상품 등록이 완료되었습니다"}, status=200)
            return Response({"message":"상품등록을 실패하였습니다", "errors": serializer.errors}, status=400)
        return Response({"message":"이 기능은 로그인을 해야만 이용할 수 있는 기능입니다."}, status=400)
    

    # 상품 목록조회
    def get(self, request):
        page = request.GET.get('page','1') # 페이지
        goods_list = Goods.objects.all()
        paginator = Paginator(goods_list, 10)
        goods = paginator.get_page(page)
        serializer = GoodsSerializer(goods.object_list, many=True)
        return Response({"전체상품 수" : paginator.count,
                        "전체 페이지" :  paginator.num_pages,
                        "현재 페이지" : goods.number,
                        "목록":serializer.data})