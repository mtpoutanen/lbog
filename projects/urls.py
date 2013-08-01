from projects.views import ProjectCreationView, ProjectCreatedView, ProjectUpdateView, \
                            ProjectUpdatedView, ProjectDetailView, RequestSentView, \
                            ProjectListView, RequestListView, RequestDetailView, \
                            NotificationsListView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^looking-for-volunteers/$',               view=ProjectCreationView.as_view(),      
        name='looking-for-volunteers'),
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
    url(r'^request-details/(?P<pk>\d+)/(?P<noti>\d+)/$',          view=RequestDetailView.as_view(),            
        name='request-details'),
    url(r'^respond-to-request/(?P<pk>\d+)/(?P<status>\w+)/$',       'projects.views.respond_to_request',
        name='respond-to-request'),
    url(r'^my-notifications/(?P<pk>\d+)/$',         view=NotificationsListView.as_view(),
        name='my-notifications'),
    )


