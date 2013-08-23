from projects.views import ProjectCreationView, ProjectCreatedView, ProjectUpdateView, \
                            ProjectUpdatedView, ProjectDetailView, HelpOfferSentView, \
                            ProjectListView, HelpOfferListView, NotificationDetailView, \
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
    url(r'^help-offer-sent/$',                         view=HelpOfferSentView.as_view(),                  
        name='help-offer-sent'),
    url(r'^my-projects/(?P<pk>\d+)/$',              view=ProjectListView.as_view(),            
        name='my-projects'),
    url(r'^my-help-offers/(?P<pk>\d+)/$',              view=HelpOfferListView.as_view(),            
        name='my-help-offers'),
    url(r'^notification-details/(?P<pk>\d+)/(?P<noti>\d+)/$',          view=NotificationDetailView.as_view(),            
        name='notification-details'),
    url(r'^respond-to-help-offer/(?P<pk>\d+)/(?P<status>\w+)/$',       'projects.views.respond_to_help_offer',
        name='respond-to-help-offer'),
    url(r'^my-notifications/(?P<pk>\d+)/$',         view=NotificationsListView.as_view(),
        name='my-notifications'),
    url(r'^get-notifications/(?P<param>\w+)/$',       'projects.views.get_notifications',
        name='get-notifications'),
    url(r'^get-help-offers/(?P<param>\w+)/$',       'projects.views.get_help_offers',
        name='get-help-offers'),
    url(r'^remove-developer/(?P<dev_id>\d+)/(?P<proj_id>\d+)/$',       'projects.views.remove_developer',
        name='remove-developer'),
    url(r'^notification-seen/(?P<pk>\d+)/$',       'projects.views.notification_seen',           
        name='notification-seen'),
    url(r'^delete-project/(?P<pk>\d+)/$',       'projects.views.delete_project',           
        name='delete-project'),
    url(r'^delete-notification/(?P<pk>\d+)/$',       'projects.views.delete_notification',           
        name='delete-notification'),
    url(r'^delete-help-offer/(?P<pk>\d+)/$',       'projects.views.delete_help_offer',           
        name='delete-help-offer'),

    )


