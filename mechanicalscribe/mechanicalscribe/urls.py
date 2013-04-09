from django.conf.urls import patterns, include, url
from django.contrib import admin
from mechanicalscribe.views import *
from mechanicalscribe.settings import DEBUG, MEDIA_ROOT, MEDIA_URL
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mechanicalscribe.views.home', name='home'),
    url(r'^notes/([A-z0-9_-]+)/$', get_note),
    url(r'^controlcenter/', include(admin.site.urls)),
    
    #url(r'^mechanicalscribe/', include('mechanicalscribe.mechanicalscribe.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls))
)

if DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
        }),
   )