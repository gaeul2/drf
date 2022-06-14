from django.contrib.auth import authenticate, login
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
# Create your views here.

class UserLoginView(APIView):
    def get(self):
        pass
    def post(self, request):#로그인
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


    class MyPageView(APIView):
        def get(self, request):
            user = request.user
            User.objects.get(id=user.id)