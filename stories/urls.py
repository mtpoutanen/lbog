from django.conf.urls import patterns, url
from stories.views import StoryDetailView

urlpatterns = patterns('',
    url(r'^story-details/(?P<pk>\d+)/$',		view=StoryDetailView.as_view(),      
        name='story-details'),
    )