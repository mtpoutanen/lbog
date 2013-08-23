from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from users.models import Country, State, Skill
from lbog.forms import ProjectSearchForm, ContactForm
from projects.models import Project
from stories.models import Story
from django.core.context_processors import csrf
from django.db.models import Q
from operator import or_, and_
import math
from django.conf import settings
from search import Search

def home(request):

    latest_completed    = Project.objects.filter(status='completed').order_by('-time_completed')[:3]
    latest_created      = Project.objects.filter(status='looking').order_by('-time_created')[:2]
    latest_stories      = Story.objects.all().order_by('-time_created')[:3]
    context                     = { 'latest_completed': latest_completed,
                                    'latest_created':   latest_created,
                                    'latest_stories':   latest_stories,
                                    }

    return render_to_response('index.html', context, context_instance=RequestContext(request))
   
def volunteers(request):
    '''
    comments
    '''
    form = ProjectSearchForm()
    context = {'form': form,}
    context.update(csrf(request))
    return render_to_response('i_want_to_help.html', context, context_instance=RequestContext(request))    

def looking_for_volunteers(request):
    '''
    comments
    '''
    form = ProjectSearchForm()
    context = {'form': form,}
    context.update(csrf(request))
    return render_to_response('looking_for_volunteers.html', context, context_instance=RequestContext(request))  

def search_projects(request):
    '''
    comments
    '''
    if request.method == 'GET':
        search      = Search(request)
        context = search.get_search_context(search.SEARCH_PROJECTS)
        return render_to_response('project_search_results.html', context)

def search_developers(request):
    '''
    comments
    '''
    if request.method == 'GET':
        search      = Search(request)
        context = search.get_search_context(search.SEARCH_DEVELOPERS)
        return render_to_response('developer_search_results.html', context)

def fbtest(request):
    fb_app_id = settings.FACEBOOK_APP_ID
    context={'fb_app_id': fb_app_id}
    return render_to_response('fbtest.html', context, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def t_and_c(request):
    return render_to_response('t_and_c.html', context_instance=RequestContext(request))

def privacy(request):
    return render_to_response('privacy_policy.html', context_instance=RequestContext(request))

def feedback(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = ['littlebitsofgood.ucl@gmail.com']

            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
        context={}
        context['form'] = form
    return render(request, 'feedback.html', context)
    # return render_to_response('feedback.html', context_instance=RequestContext(request))
