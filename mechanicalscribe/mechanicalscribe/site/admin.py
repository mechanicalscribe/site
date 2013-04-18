from pagedown.widgets import AdminPagedownWidget
from django.contrib import admin
from django.conf import settings
from models import Member, Sticky, StickyTemplate
from django import forms

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first', 'last')
    save_on_top = True
    ordering = ('-last',)

class StickyModelForm(forms.ModelForm):
    description_markdown = forms.CharField(widget=AdminPagedownWidget())        
    class Meta:
        model = Sticky

class StickyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    form = StickyModelForm

class StickyTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', )
    form = StickyModelForm

admin.site.register(Member, MemberAdmin)
admin.site.register(Sticky, StickyAdmin)
admin.site.register(StickyTemplate, StickyTemplateAdmin)