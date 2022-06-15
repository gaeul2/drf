from django.urls import path
from . import views

app_label = 'user'
urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='login'),
    path('user_info', views.UserInfoView.as_view(), name='user_info'),
    path('find/same_hobby', views.SameHobbyUserView.as_view(), name='find_same_hobby'),
    path('show/login_user', views.LoginUserInfoView.as_view(), name='login_user_info'),
]