from django.template import Library, Node
from projects.models import RequestNotification

register = Library()

class NewNotificationsNode(Node):
    def __init__(self, num):
        self.num = num
    
    def render(self, context):
    	user   = context['request'].user
        if user.id:
            # user.id = 0
            context['notifications'] = RequestNotification.objects.filter(receiver=user.get_profile()).order_by('-time_created')
            context['new_notifications'] = RequestNotification.objects.filter(receiver=user.get_profile(), seen=False)
        else:
            context['notifications'] = []
            context['new_notifications'] = []
        
        return ''

def get_new_notifications(parser, token):
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, "get_new notifications tag takes exactly one argument"
    return NewNotificationsNode(bits[1])

get_new_notifications = register.tag(get_new_notifications)