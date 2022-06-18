from django.db import models
from user.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=50)
    explain = models.TextField("카테고리 설명")

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, related_name='article', on_delete=models.CASCADE)
    title = models.CharField("글 제목", max_length=100, blank=False, null=False)
    category = models.ManyToManyField(to=Category, verbose_name="카테고리")
    content = models.TextField("글 내용", blank=False, null=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField("댓글 내용",max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        self.comment


