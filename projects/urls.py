from projects.views import ProjectCreationView, ProjectCreatedView, ProjectUpdateView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^looking-for-volunteers/$',               view=ProjectCreationView.as_view(),      
        name='looking-for-volunteers'),
    url(r'^project-created/$',						view=ProjectCreatedView.as_view(),                  
        name='project-created'),
    url(r'^update-project-details/(?P<pk>\d+)/$', 	view=ProjectUpdateView.as_view(),            
        name='update-project-details'),
    url(r'^charity-data/(?P<pk>\d+)/$', 			'projects.views.charity_data',            
        name='charity-data'),
    )