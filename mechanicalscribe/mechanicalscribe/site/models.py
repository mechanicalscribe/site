from django.db import models

class Member(models.Model):
    user_name = models.CharField(max_length=18)
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=40)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    facebook = models.CharField(max_length=30, blank=True)    
    avatar = models.ImageField(upload_to='img/thumbnails/', blank=True, null=True)
    def __unicode__(self):
        return u'%s %s' % (self.first, self.last)

class StickyTemplate(models.Model):
    name = models.CharField(max_length=18)
    template_name = models.CharField(max_length=18, default="list.html")
    description_markdown = models.TextField('Description as Markdown')
    code = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.name)

class Sticky(models.Model):
    name = models.CharField(max_length=18)
    description_markdown = models.TextField('Description as Markdown')
    template = models.ForeignKey(StickyTemplate, blank=True, null=True)    
    code = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.name)

'''
class Library(models.Model):
    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)
    license = models.CharField(max_length=50)
'''

class Homepage(models.Model):
    title = models.CharField(max_length=50)
    code = models.TextField(blank=True)
    def __unicode__(self):
        return u'%s' % (self.title)
    
class ActiveHomepage(models.Model):
    active_page = models.ForeignKey(Homepage)
    def __unicode__(self):
        return u'%s' % ("Active Homepage")
