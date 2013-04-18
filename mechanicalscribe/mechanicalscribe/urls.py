from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from mechanicalscribe.views import *
from mechanicalscribe.settings import DEBUG, MEDIA_ROOT, MEDIA_URL
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', get_home),
    (r'^notes/([A-z0-9_-]+)/$', get_note),
    (r'^controlcenter/', include(admin.site.urls)),
    (r'^about|contact/$', TemplateView.as_view(template_name="about.html")),
    (r'^([A-z0-9_-]+)/$', get_sticky),
    
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