import os 
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db.models import permalink
from django.contrib.auth.models import User
from django.conf import settings
from mechanicalscribe.site.models import Member, Sticky

import datetime
import markdown

def get_upload_path(instance, filename):
    print instance.page.slug, filename
    path = os.path.join("files", instance.page.slug, filename)
    print path
    return path

def get_img_path(instance, filename):
    print instance.slug, filename
    path = os.path.join("files", instance.slug, filename)
    print path
    return path

class Note(models.Model):
    #basics
    title = models.CharField('title', max_length=250)
    slug = models.SlugField('slug', max_length=250)
    author = models.ForeignKey(Member, blank=True, null=True)
    short_title = models.CharField('short_title', max_length=100)
    
    #timestamps
    created = models.DateTimeField('created', auto_now_add=True)
    published = models.DateTimeField('published', default=datetime.datetime.now)
    modified = models.DateTimeField('modified', auto_now=True)

    #options
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public'),
    )
    status = models.IntegerField('status', choices=STATUS_CHOICES, default=2)
    allow_comments = models.BooleanField('allow comments', default=True)
    stickies = models.ManyToManyField(Sticky, null=True)

    teaser = models.TextField('Teaser as HTML', blank=True, null=True)

    #copy    
    body_markdown = models.TextField('Entry body as Markdown', blank=True, null=True)
    body = models.TextField('Entry body as HTML', blank=True, null=True)

    #page elements
    styles = models.TextField('stylesheets or inline styles to add to head. Include <link> or <style> tags.', blank=True, null=True)
    code = models.TextField('Javascript to run at end of <body>. Include <script> tags.', blank=True, null=True)

    #display properties
    homepage_width = models.IntegerField(blank=True, null=True)
    homepage_priority = models.IntegerField(default=0, blank=True, null=True)

    #server-side python code
    python = models.TextField('Python to run prior to page load. Output passed to page as data object.', blank=True, null=True)
        
    #files
    stills = models.ImageField(upload_to=get_img_path, blank=True, null=True)
    #files = models.ManyToManyField(File, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.title, self.slug)

    def save(self): 
        self.body = markdown.markdown(self.body_markdown)
        super(Note, self).save() # Call the "real" save() method.   

class File(models.Model):
    name = models.CharField('title', max_length=50, default="")
    page = models.ForeignKey('Note', default="")
    file = models.FileField(upload_to=get_upload_path)
    
    def __unicode__(self):
        return u'%s' % (self.name)