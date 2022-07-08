from django.contrib import admin
from .models import Event as EventModel
from django.utils.safestring import mark_safe


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'explain',
        'created_date',
        'show_stop_date',
        'is_active',
        'thumbnail_preview'
    )

    def thumbnail_preview(self, obj):
        return mark_safe(f'<img src="/thumbnail/{obj.id}" height="100px"/>') #이미지 src를 우리가 지정해준 url로!
    thumbnail_preview.short_dexcription = "Thumbnail"

admin.site.register(EventModel, EventAdmin)
