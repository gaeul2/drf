from django.db import models
from user.models import User as UserModel
# Create your models here.
class Event(models.Model):
    title = models.CharField("제목", max_length=100)
    thumbnail = models.ImageField("썸네일", upload_to="static/img/product/thumbnail", height_field=None, width_field=None, max_length=None)
    explain = models.TextField("설명")
    created_date = models.DateTimeField("등록일자",auto_now_add=True)
    show_start_date = models.DateField("노출시작일")
    show_stop_date = models.DateField("노출 종료일")
    is_active = models.BooleanField("활성화 여부",default=0)

    def __str__(self):
        return self.title


class product(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField("상품이름", max_length=250)
    thumbnail = models.ImageField("썸네일", upload_to="static/img/product")
    explain = models.TextField("상품설명")
    created_date = models.DateTimeField("등록일자", auto_now_add=True)
    updated_date = models.DateTimeField("수정일자", auto_now=True)
    show_start_date = models.DateField("노출시작일")
    show_stop_date = models.DateField("노출 종료일")
    price = models.IntegerField("가격")
    is_active = models.BooleanField("활성화 여부", default=0)

    def __str__(self):
        return self.name
