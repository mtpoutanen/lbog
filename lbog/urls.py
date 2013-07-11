from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^account/', include('users.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'lbog.views.home', name='home'),
    
    # (r'^/media/(?P<path>.*)$', 'django.views.static.serve',
        # {'document_root': settings.MEDIA_ROOT})
)
