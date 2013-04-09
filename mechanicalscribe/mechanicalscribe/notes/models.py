from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.conf import settings
from mechanicalscribe.site.models import Member

import datetime
import markdown

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
    #categories = models.ManyToManyField(Category, blank=True)    

    #copy    
    body_markdown = models.TextField('Entry body as Markdown', blank=True, null=True)
    body = models.TextField('Entry body as HTML', blank=True, null=True)
    
    def save(self):
        self.body = markdown.markdown(self.body_markdown)
        super(Note, self).save() # Call the "real" save() method.    