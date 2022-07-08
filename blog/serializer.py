from rest_framework import serializers
from .models import Article as ArticleModel



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ["title", "category", "content"]