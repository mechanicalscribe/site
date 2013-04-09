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

class Homepage(models.Model):
    title = models.CharField(max_length=50)
    code = models.TextField(blank=True)
    def __unicode__(self):
        return u'%s' % (self.title)
    
class ActiveHomepage(models.Model):
    active_page = models.ForeignKey(Homepage)
    def __unicode__(self):
        return u'%s' % ("Active Homepage")
