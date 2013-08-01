from django.conf.urls import patterns, include, url
from django.conf import settings
# from lbog.views import VolunteerView
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        # (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
    url(r'^accounts/', include('users.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^stories/', include('stories.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'lbog.views.home', name='home'),
    url(r'^i-want-to-help/$',     'lbog.views.volunteers',                  
        name='i-want-to-help'),
    url(r'^search-projects/$',     'lbog.views.search_projects',                  
        name='search-projects'),
    # url(r'^js_reverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),
    # (r'^facebook/', include('django_facebook.urls')),
    # url(r'^jsurls.js$', 'django_js_utils.views.jsurls', {}, 'jsurls'),
    # (r'^/media/(?P<path>.*)$', 'django.views.static.serve',
        # {'document_root': settings.MEDIA_ROOT})
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)