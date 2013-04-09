from django.db import models
from mechanicalscribe.site.models import Member
from tinymce import models as tinymce_models
#from django.core.files.storage import FileSystemStorage

import datetime
import markdown

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.name)

#fs = FileSystemStorage(location='media/img/thumbnails/')
 
class Interactive(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=100, blank=True)
    thumbnail = models.ImageField(upload_to='img/thumbnails', blank=True, null=True)
    authors = models.ManyToManyField(Member, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name="interactive", blank = True, null=True)
    page_width = models.IntegerField(default='600')
    credit = tinymce_models.HTMLField(default="",blank=True)
    extra_head = models.TextField(default="",blank=True, null=True)
    intro = tinymce_models.HTMLField(default="",blank=True, null=True)
    code = models.TextField(default="",blank=True)
    show_on_toc = models.BooleanField(default=True, blank=True)
    importance = models.IntegerField(default=0, blank=True, null=True)
	
    def __unicode__(self):
        return u'%s' % (self.title)
