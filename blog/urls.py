from django.urls import path
from . import views

urlpatterns = [
    path('create/article/<int:id>', views.WriteArticleView.as_view(), name='create_article')
]