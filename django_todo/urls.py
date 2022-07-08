from django.urls import path
from django_todo import views


urlpatterns = [
    path('todo/', views.show_not_complete_todos, name='todo_list'),
    path('todo/<int:pk>', views.todo_detail, name='todo_detail'),
    path('todo/post', views.create_todo, name='todo_post'),
]