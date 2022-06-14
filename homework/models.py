from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField('가수이름', max_length=20)
    gender = models.BooleanField('성별(True가 여)')
    solo = models.BooleanField('솔로 혹은 그룹')

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField('노래제목',max_length=25)
    lyrics = models.TextField('가사')
    singer = models.OneToOneField(to=Singer, verbose_name='원곡자', on_delete=models.CASCADE)
    remake_singer = models.ManyToManyField(to=Singer, verbose_name='리메이크 가수', related_name='remake_singer')
    release_date = models.DateTimeField('발매일')

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField("장르", max_length=30)

    def __str__(self):
        return self.name

# class User(models.Model):
#     username = models.CharField("사용자 계정", max_length=20, unique=True)
#     password = models.CharField("비밀번호", max_length=60)
#     level = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.username