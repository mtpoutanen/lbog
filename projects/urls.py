from projects.views import ProjectCreationView, ProjectCreatedView, ProjectUpdateView, \
                            ProjectUpdatedView, ProjectDetailView, RequestSentView, \
                            ProjectListView, RequestListView, NotificationDetailView, \
                            NotificationsListView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^create-new-project/$',               view=ProjectCreationView.as_view(),      
        name='create-new-project'),
    url(r'^project-created/$',						view=ProjectCreatedView.as_view(),                  
        name='project-created'),
    url(r'^update-project-details/(?P<pk>\d+)/$', 	view=ProjectUpdateView.as_view(),            
        name='update-project-details'),
    url(r'^project-updated/$',						view=ProjectUpdatedView.as_view(),                  
        name='project-updated'),
    url(r'^project-details/(?P<pk>\d+)/$',          view=ProjectDetailView.as_view(),                  
        name='project-details'),
    url(r'^request-sent/$',                         view=RequestSentView.as_view(),                  
        name='request-sent'),
    url(r'^my-projects/(?P<pk>\d+)/$',              view=ProjectListView.as_view(),            
        name='my-projects'),
    url(r'^my-requests/(?P<pk>\d+)/$',              view=RequestListView.as_view(),            
        name='my-requests'),
    url(r'^notification-details/(?P<pk>\d+)/(?P<noti>\d+)/$',          view=NotificationDetailView.as_view(),            
        name='notification-details'),
    url(r'^respond-to-request/(?P<pk>\d+)/(?P<status>\w+)/$',       'projects.views.respond_to_request',
        name='respond-to-request'),
    url(r'^my-notifications/(?P<pk>\d+)/$',         view=NotificationsListView.as_view(),
        name='my-notifications'),
    url(r'^get-notifications/(?P<param>\w+)/$',       'projects.views.get_notifications',
        name='get-notifications'),
    url(r'^get-requests/(?P<param>\w+)/$',       'projects.views.get_requests',
        name='get-requests'),
    url(r'^remove-developer/(?P<dev_id>\d+)/(?P<proj_id>\d+)/$',       'projects.views.remove_developer',
        name='remove-developer'),
    url(r'^notification-seen/(?P<pk>\d+)/$',       'projects.views.notification_seen',           
        name='notification-seen'),

    )


