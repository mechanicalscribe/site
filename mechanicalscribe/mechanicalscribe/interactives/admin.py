from django.contrib import admin
from django.conf import settings
from models import Interactive, Category
from AdminImage import AdminImageWidget

class InteractiveAdmin(admin.ModelAdmin):
    #class Media:
    #    js = ('/home/chris/Dropbox/Private/django/mechanicalscribe/static/js/tiny_mce.js', '/home/chris/Dropbox/Private/django/mechanicalscribe/static/js/textareas.js''http://labs.slate.com/media/js/tiny_mce/textareas.js') 
    save_on_top = True
    ordering = ('title',)
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'thumbnail':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(InteractiveAdmin,self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Category)
admin.site.register(Interactive, InteractiveAdmin)
#admin.site.register(Homepage)
#admin.site.register(ActiveHomepage)

