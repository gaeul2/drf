from django.urls import path
from . import views

urlpatterns = [
    path('create/article/<int:id>', views.WriteArticle.as_view(), name='create_article')
]