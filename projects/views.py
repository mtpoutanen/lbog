from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView, UpdateView
from projects.forms import ProjectCreationForm, ProjectChangeForm, RequestForm
from projects.models import Project, Request, RequestNotification
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django import forms
from django.utils import simplejson
from django.core.urlresolvers import reverse_lazy

class CorrectUserMixin(object):

    error_message           = 'You are logged in as the wrong user. \
                                No detailed error message was provided'
    url_id                  = 0 # default value

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response with a template rendered with the given context.
        """
        logged_in_id        = self.request.user.id
        if self.url_id == 0:
            raise ImproperlyConfigured("url_id missing")

        if logged_in_id == int(self.url_id):
            return self.response_class(
                request = self.request,
                template = self.get_template_names(),
                context = context,
                **response_kwargs
            )
        else:
            context['error_message'] = self.error_message
            return self.response_class(
                request = self.request,
                template = 'wrong_user.html',
                context = context,
                **response_kwargs
            )

class ProjectCreationView(FormView):
    model           = Project
    template_name   = 'looking_for_volunteers.html'
    form_class      = ProjectCreationForm
    success_url     = reverse_lazy('project-created')

    def form_valid(self, form):
        profile                 = self.request.user.get_profile()
        if profile.user_type != 'Charity':
            raise forms.ValidationError('You must log in as a Charity to upload projects')
        form.instance.charity   = profile
        form.instance.status    = 'looking'
        form.save()

        return super(ProjectCreationView, self).form_valid(form)

class ProjectCreatedView(TemplateView):
    template_name   = 'project_created.html'

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model           = Project
    login_url       = reverse_lazy('login-required')
    template_name   = 'change_project_details.html'
    form_class      = ProjectChangeForm
    success_url     = reverse_lazy('project-updated')

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """ 
        super(ProjectUpdateView, self).get_initial()
        project_id      = self.kwargs['pk']
        project         = Project.objects.get(pk=project_id) 
        skill_list      = project.skills
        status          = project.status
        initial = {
            'skills':   list(skill_list.all()),
            'status':   status,  
        }
        return initial

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response with a template rendered with the given context.
        """
        project             = Project.objects.get(id=self.kwargs['pk'])
        charity_id          = project.charity.id
        logged_in_id        = self.request.user.id


        if logged_in_id == int(charity_id):
            return self.response_class(
                request = self.request,
                template = self.get_template_names(),
                context = context,
                **response_kwargs
            )
        else:
            context['error_message'] = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s project.'
            return self.response_class(
                request = self.request,
                template = 'wrong_user.html',
                context = context,
                **response_kwargs
            )


class ProjectUpdatedView(TemplateView):
    template_name = 'project_updated.html'


class ProjectDetailView(FormView):
    model           = Request
    template_name   = 'project_details.html'
    form_class      = RequestForm
    success_url     = reverse_lazy('request-sent')

    def get_context_data(self, **kwargs):
        project_id  = self.kwargs['pk']
        project     = Project.objects.get(id=project_id)
        return {
            'form':     self.get_form(self.form_class),
            'params':   kwargs,
            'project':  project,
        }
    
    def form_valid(self, form):
        'render nothing if not the right user'
        profile                 = self.request.user.get_profile()
        if profile.user_type    != 'Developer':
            raise forms.ValidationError('You must log in as a Developer to offer your help on projects')
        form.instance.sender    = profile
        project_id              = self.kwargs['pk']
        project                 = Project.objects.get(id=project_id)
        form.instance.project   = project
        request                 = form.save()
        notification            = RequestNotification.objects.create(
                sender          = profile,
                receiver        = project.charity,
                request         = request,
                seen            = False,
            ) 
        return super(ProjectDetailView, self).form_valid(form)

class RequestSentView(LoginRequiredMixin, TemplateView):
    template_name   = 'request_sent.html'

class ProjectListView(LoginRequiredMixin, CorrectUserMixin, TemplateView):
    template_name = 'my_projects.html'
    error_message = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s project list.'

    def get_context_data(self, **kwargs):
        
        self.url_id              = self.kwargs['pk']
        my_id       = self.request.user.id
        projects    = Project.objects.filter(charity = my_id)
        return {
            'params':   kwargs,
            'projects': projects,
        }

class RequestListView(LoginRequiredMixin, CorrectUserMixin, TemplateView):

    error_message       = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s request list.'
    def get_context_data(self, **kwargs):

        self.url_id              = self.kwargs['pk']
        my_id       = self.request.user.id
        
        if self.request.user.get_profile().user_type == 'Charity':
            self.template_name = 'my_requests_charity.html'
            requests    = Request.objects.filter(project__charity__id = my_id).order_by('-time_created')
        else:
            self.template_name = 'my_requests_developer.html'
            requests    = Request.objects.filter(sender__id = my_id).order_by('-time_created')
        return {
            'params':   kwargs,
            'requests': requests,
        }

class RequestDetailView(LoginRequiredMixin, CorrectUserMixin, TemplateView):

    template_name       = 'request_details.html'
    error_message       = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s request.'

    def get_context_data(self, **kwargs):

        request_id          = int(self.kwargs['pk'])
        noti_id             = int(self.kwargs['noti'])
        notification        = RequestNotification.objects.get(id=noti_id)
        notification.seen   = True
        notification.save()
        my_request      = Request.objects.get(id=request_id)
        if self.request.user.get_profile().user_type == 'Charity':
            self.url_id     = my_request.project.charity.id
        else:
            self.url_id     = my_request.sender.id   
        return {
            'test_var': request_id,
            'params':   kwargs,
            'my_request':  my_request,
        }


def respond_to_request(request, pk, status):
    '''
    Accepts a Developer's request to help on a project
    and creates a notification to the Developer.
    '''
    request_id      = pk
    my_request      = Request.objects.get(id=request_id)
    project_owner   = my_request.project.charity

    if request.user.id != project_owner.id:
        result =    {
                    'error_message': 'Something went wrong, this project belongs to user '+project_owner.user.username, 
                    'status': '' 
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        my_request.status   = status
        my_request.save()
        notification        = RequestNotification.objects.create(
                sender      = project_owner,
                receiver    = my_request.sender,
                request     = my_request,
                seen        = False,
            ) 
        result =    { 
                    'status': status,
                    'error_message': '',
                    }
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

class NotificationsListView(LoginRequiredMixin, CorrectUserMixin, TemplateView):

    error_message = 'Oops, something went wrong. \
                    The browser was trying to access someone else\'s notification list.'
    template_name = 'my_notifications.html'

    def get_context_data(self, **kwargs):
        
        self.url_id          = self.kwargs['pk']
        my_id           = self.request.user.id
        notifications   = RequestNotification.objects.filter(request__sender__id = my_id).order_by('-time_created')
        return {
            'params':   kwargs,
            'notifications': notifications,
        }

       