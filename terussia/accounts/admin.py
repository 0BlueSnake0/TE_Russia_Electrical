from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin 
from django.utils.safestring import mark_safe 
from django.contrib.auth.models import Group 

from .models import *

admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
                    'get_avatar',
                    'username',
                    'email',  
                    'is_staff', 
                    'is_admin',  
    ]
    list_filter = ['last_login', 'is_admin']
    add_fieldsets = [
        (None, {'fields': ('username', 'email', 'password1', 'password2','avatar'),}),
    ]
    fieldsets = [
        ('Username', {'fields': ('username',)}),
        ('Email', {'fields': ('email',)}),
        ('Avatar', {'fields': ('avatar',)}),
        ('Permissions', {'fields': ('is_admin','is_staff')}), 
    ]
    filter_horizontal = [] 
     
    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src="{obj.avatar.url}" style="border-radius:50%;" width="50px" height="50px">'
                )
    get_avatar.short_description = 'Profile photo'
  