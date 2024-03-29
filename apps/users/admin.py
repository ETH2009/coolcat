from django.contrib import admin
from .models import User

admin.site.site_header = "CoolCat管理后台"
admin.site.site_title = "CoolCat"
admin.site.index_title = "欢迎访问CoolCat后台系统"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """用户后台管理"""
    list_display = ('username', 'id', 'email', 'mobile', 'date_joined', 'last_login')
    search_fields = ('username', 'email', 'mobile')
    list_filter = ('gender', 'birthday')
    ordering = ('id',)
