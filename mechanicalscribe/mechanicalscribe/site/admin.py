from django.contrib import admin
from django.conf import settings
from models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first', 'last')
    save_on_top = True
    ordering = ('-last',)

admin.site.register(Member, MemberAdmin)