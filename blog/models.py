from django.db import models
from user.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=50)
    explain = models.TextField("카테고리 설명")

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("글 제목", max_length=100, blank=False, null=False)
    category = models.ManyToManyField(to=Category, verbose_name="카테고리")
    content = models.TextField("글 내용", blank=False, null=False)

    def __str__(self):
        return self.title

