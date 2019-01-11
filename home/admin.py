from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # empty_value_display = '-empty-'
    list_display = ('name', 'name_chn', 'nick_name', 'number', 'grade', 'top_star', 'all_pos', 'stamina', 'athletic')


