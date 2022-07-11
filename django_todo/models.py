from django.db import models

# Create your models here.
class DjangoTodo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=0)
    important = models.BooleanField(default=0)

    def __str__(self):
        return self.title