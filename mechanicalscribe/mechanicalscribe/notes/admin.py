from pagedown.widgets import AdminPagedownWidget
from AdminImageWidget import AdminImageWidget
from django.contrib import admin
from mechanicalscribe.notes.models import Note, File
from django import forms

class NoteModelForm(forms.ModelForm): 
    body_markdown = forms.CharField(widget=AdminPagedownWidget())        
    class Meta:
        model = Note

class NoteFileInline(admin.TabularInline):
    model = File

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    form = NoteModelForm
    inlines = [NoteFileInline,]        
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'stills':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(NoteAdmin,self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Note, NoteAdmin)
