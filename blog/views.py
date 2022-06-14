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
        return bool(request.user and request.user.join_date <= (timezone.now() - timedelta(days=3)))
        #3시간이상인 사용자만 접근가능할때
        # return bool(request.user and request.user.join_date <= (timezone.now() - timedelta(hours=3)))
class WriteArticle(APIView):

    permission_classes = [WriteAfterThreeDaysOfSubscription]
    def post(self, request, id):
        user = User.objects.get(id=id)
        title = request.data.get('title', '')
        input_category = request.data.get('category', '')
        content = request.data.get('content', '')
        try:
            category = Category.objects.get(name='수다')
        except Category.DoesNotExist:
            Category.objects.create(name=input_category)
        else:
            article = Article.objects.create(
                author=user,
                title=title,
                content=content
            )
            article.save()
            return Response({"message": f'게시글 {article.title}이 잘 작성되었습니다.'})
        #카테고리 를 article만들면서 넣으면 에러남..