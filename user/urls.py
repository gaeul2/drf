from django.urls import path
from . import views

app_label = 'user'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login')
]