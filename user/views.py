from django.contrib.auth import authenticate, login
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Article, Category
from .models import User
from django.contrib.auth.hashers import make_password
from user.serializer import UserSerializer

# Create your views here.

class UserLoginView(APIView):
    def post(self, request):  # 로그인
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        hashed_pass = make_password(password)
        edit_user = User.objects.get(username=username)
        edit_user.password = hashed_pass
        edit_user.save()
        user = authenticate(request, username=username, password=password)
        # signup을 만들지 않고 admin에서 유저생성을 했기때문에 암호화된 비밀번호가 아니여서 장고가 인증을 못함.
        # make_password() 함수를 통해 비밀번호를 해쉬화해서 해당유저 비밀번호를 변경하고, 인증을 시도하면 로그인 가능.

        if user is None:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


class UserInfoView(APIView):
    def get(self, request):
        user = request.user
        articles = Article.objects.filter(author=user)
        article_list = []
        for article in articles:
            article_list.append(str(article))
        context = {"username": user.username, "user_fullname": user.fullname, 'articles':article_list}
        return Response({"message":context})

class SameHobbyUserView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        '''
        모든 사용자에 대해 user정보와 userprofile정보 가져오고
        같은 취미를 가진 사람들 출력하기
        '''

        user_serializer = UserSerializer(User.objects.all(), many=True).data
        return Response(user_serializer, status=status.HTTP_200_OK)


