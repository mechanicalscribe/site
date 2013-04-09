from pagedown.widgets import AdminPagedownWidget
from django.contrib import admin
from mechanicalscribe.notes.models import Note
from django import forms

class NoteModelForm(forms.ModelForm):
    body_markdown = forms.CharField(widget=AdminPagedownWidget())        
    class Meta:
        model = Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    form = NoteModelForm

admin.site.register(Note, NoteAdmin)