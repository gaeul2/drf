from django.contrib import admin
from .models import Song as SongModel
from .models import Singer as SingerModel
from .models import Genre as GenreModel

# Register your models here.
admin.site.register(SingerModel)
admin.site.register(SongModel)
admin.site.register(GenreModel)