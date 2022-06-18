from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Article, Category
from .models import User
from datetime import timedelta
from django.utils import timezone

# Create your views here.

class WriteAfterThreeDaysOfSubscription(BasePermission):
    '''
    가입일 기준 3일이상 지난 사용자만 접근가능
    '''
    message = '가입일 기준 3일이상 지난 사용자만 접근가능합니다.'

    def has_permission(self, request, view):
        # return bool(request.user and request.user.join_date <= (timezone.now() - timedelta(days=3)))
        #3시간이상인 사용자만 접근가능할때
        return bool(request.user and request.user.join_date <= (timezone.now() - timedelta(hours=3)))


class WriteArticleView(APIView):
    permission_classes = [WriteAfterThreeDaysOfSubscription]
    def post(self, request, id):
        user = User.objects.get(id=id)
        title = request.data.get('title', '')
        input_category = request.data.get('category', '').split(',')
        content = request.data.get('content', '')
        article = Article.objects.create(
            author=user,
            title=title,
            content=content,
        )
        for i in input_category:
            article.category.add(i)
        return Response({"message": f'게시글 {article.title}이 잘 작성되었습니다.'})
        # try:
        #     Category.objects.get(name=input_category)
        # except Category.DoesNotExist:
        #     category=Category.objects.create(name=input_category)
        #     article.category.set(category)
        #     return Response({"message": f'게시글 {article.title}이 잘 작성되었습니다.'})
        # else:
        #     article.category.set(input_category)
        #     return Response({"message": f'게시글 {article.title}이 잘 작성되었습니다.'})
