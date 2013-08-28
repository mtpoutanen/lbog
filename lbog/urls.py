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
    url(r'^fbtest/$',                   'lbog.views.fbtest',            name='fbtest'),
    url(r'^$',                          'lbog.views.home',              name='home'),
    url(r'^i-want-to-help/$',           'lbog.views.volunteers',        name='i-want-to-help'),   
    url(r'^looking-for-volunteers/$',   'lbog.views.looking_for_volunteers',  name='looking-for-volunteers'),   
    url(r'^search-projects/$',          'lbog.views.search_projects',   name='search-projects'),
    url(r'^search-developers/$',        'lbog.views.search_developers',   name='search-developers'),
    url(r'^about/$',                    'lbog.views.about',             name='about'),
    url(r'^feedback/$',                 'lbog.views.feedback',          name='feedback'),
    url(r'^t_and_c/$',                  'lbog.views.t_and_c',           name='t-and-c'),
    # url(r'^privacy/$',                  'lbog.views.privacy',           name='privacy'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)