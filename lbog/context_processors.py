from django.conf import settings # import the settings file

def fb_app_id(request):
	'''makes facebook app id accessible in templates '''
	return {
    	'FB_APP_ID': settings.FACEBOOK_APP_ID,
    	'SITE_ROOT': settings.ALLOWED_HOSTS[0],
    	}