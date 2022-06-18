from django.contrib.auth.models import Group

from django.contrib import admin
from .models import User, UserProfile, Hobby
# Register your models here.
admin.site.unregister(Group)

class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'fullname') #사용자 목록에 보여질 필드지정
    list_display_links = ('username',) #상세페이지 눌러서 들어갈 필드지정
    list_filter = ('username',) # filter를 걸 수 있는 필드를 생성한다.

    inlines = (
        UserProfileInline,
    )
admin.site.register(User, UserAdmin)
# admin.site.register(UserProfile)
admin.site.register(Hobby)