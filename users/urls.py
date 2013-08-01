from users.views import LoginView, LoginSuccessfulView, LoginRequiredView, RegSuccessView, \
                        RegistrationView, ChangeView, SuccessView, CharityView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^register/$',               view=RegistrationView.as_view(),      
        name='register'),
    url(r'^registration-successful/$',view=RegSuccessView.as_view(),                  
        name='registration-successful'),
    url(r'^login/$',                  view=LoginView.as_view(),             
        name='login'),
    url(r'^login-required/$',         view=LoginRequiredView.as_view(),     
        name='login-required'),
    url(r'^logged-in/$',              view=LoginSuccessfulView.as_view(),   
        name='logged-in'),
    url(r'^my-account/(?P<pk>\d+)/$', view=ChangeView.as_view(),            
        name='my-account'),
    url(r'^profile-changed/$',        view=SuccessView.as_view(),           
        name='profile-changed'),
    url(r'^password-change-done/$',   'django.contrib.auth.views.password_change_done',
        name='password-change-done'),
    url(r'^password-change/$',        'django.contrib.auth.views.password_change',   
        name='password-change'),
    url(r'^logout/$',                 'django.contrib.auth.views.logout',   
                                      {'next_page': '/accounts/login/'},    name='logout'),
    url(r'^charity-details/(?P<pk>\d+)/$', view=CharityView.as_view(),            
        name='charity-details'),
)


