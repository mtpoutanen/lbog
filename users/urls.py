from users.views import LoginView, LoginSuccessfulView, RegistrationView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^register/$', view=RegistrationView.as_view(), name='register'),
    url(r'^login/$', view=LoginView.as_view(), name='login'),
    url(r'^logged-in/$', view=LoginSuccessfulView.as_view(), name='logged-in'),
)


