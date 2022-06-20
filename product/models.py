from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField("제목", max_length=100)
    thumbnail = models.URLField("썸네일")
    explain = models.TextField("설명")
    created_date = models.DateTimeField("등록일자",auto_now_add=True)
    show_start_date = models.DateTimeField("노출시작일")
    show_stop_date = models.DateTimeField("노출 종료일")
    alive = models.BooleanField("활성화 여부",default=0)

