from django.conf import settings # import the settings file

def fb_app_id(request):
    return {'FB_APP_ID': settings.FACEBOOK_APP_ID}