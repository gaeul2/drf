import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Song, Singer

class Login_and_Level_Check(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.level >=3)



class SongView(APIView):
    # 클래스 접근권한
    # permission_classes = [Login_and_Level_Check]
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        all_songs = Song.objects.all()
        context = {
            'message': 'get method!',
            'songs' : str(all_songs),
        }
        return Response(context)

    def post(self, request):
        singer = Singer.objects.create(name='옥상달빛', gender=1, solo=0)
        context = {
            'message': 'post method!',
            'OK' : f"가수 {str(singer)}가(이) 추가되었습니다."
        }
        return Response(context)

    def put(self, request):
        return Response({'message':'put method!'})

    def delete(self, request):
        return Response({'message':'delete method!'})