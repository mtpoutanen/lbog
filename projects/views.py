from django.shortcuts import render_to_response
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.models import User
from projects.forms import ProjectCreationForm, ProjectChangeForm, RequestForm
from projects.models import Project, Request, RequestNotification
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django import forms
from django.utils import simplejson
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

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

class ProjectCreationView(LoginRequiredMixin, FormView):
    model           = Project
    template_name   = 'create_new_project.html'
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

class ProjectUpdateView(LoginRequiredMixin, CorrectUserMixin, UpdateView):
    model           = Project
    login_url       = reverse_lazy('login-required')
    template_name   = 'change_project_details.html'
    form_class      = ProjectChangeForm
    success_url     = reverse_lazy('project-updated')
    error_message   = 'Oops, something went wrong. \
            The browser was trying to update someone else\'s project.'

    def get_context_data(self, **kwargs):
        context                 = super(ProjectUpdateView, self).get_context_data(**kwargs)
        project_id              = self.kwargs['pk']
        project                 = Project.objects.get(pk=project_id) 
        project_developers      = project.developers.all()
        context['project_id']   = project.id 
        context['developers']   = project_developers
        return context

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

        self.url_id     = project.charity.id
        return initial

class ProjectUpdatedView(TemplateView):
    template_name = 'project_updated.html'

class ProjectDetailView(FormView):
    model           = Request
    template_name   = 'project_details.html'
    success_url     = reverse_lazy('request-sent')
    
    def get_form(self, form_class):
        form_class              = RequestForm
        form = super(ProjectDetailView, self).get_form(form_class)
        form.view_request       = self.request
        form.view_request_pk    = self.kwargs['pk']
        return form

    def get_context_data(self, **kwargs):
        context                         = super(ProjectDetailView, self).get_context_data(**kwargs)       
        project_id                      = self.kwargs['pk']
        project                         = Project.objects.get(id=project_id)
        context['form']                 = self.get_form(self.form_class)
        context['params']               = kwargs
        context['project']              = project
        context['already_requested']    = False

        if self.request.user.is_authenticated():
            my_id                           = self.request.user.id
            # using filter instead of get just in case someone creates a second request in admin etc.
            this_project_requested          = Request.objects.filter(sender__id=my_id, project=project)
            context['already_requested']    = this_project_requested

        return context
    
    def form_valid(self, form):
        import pdb
        pdb.set_trace();
        'render nothing if not the right user'
        profile                 = self.request.user.get_profile()
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
    error_message = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s project list.'

    def get_context_data(self, **kwargs):
        
        user_type   = self.request.user.get_profile().user_type
        my_id       = self.request.user.id
        if user_type == 'Charity':
            projects            = Project.objects.filter(charity = my_id).order_by('-time_created')
            self.template_name  = 'my_projects_charity.html'
        else:
            all_projects        = Project.objects.all().order_by('-time_created')
            my_profile          = User.objects.get(id=my_id).get_profile()
            projects            = filter(lambda project: my_profile in project.developers.all(), all_projects)
            self.template_name  = 'my_projects_developer.html'

        self.url_id             = self.kwargs['pk']
        return {
            'params':   kwargs,
            'projects': projects,
        }

class RequestListView(LoginRequiredMixin, CorrectUserMixin, TemplateView):

    template_name       = 'my_requests.html'
    error_message       = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s request list.'
    def get_context_data(self, **kwargs):

        self.url_id     = self.kwargs['pk']
        my_id           = self.request.user.id
        
        if self.request.user.get_profile().user_type == 'Charity':
            template_name_requests = 'requests_charity_content.html'
            requests    = Request.objects.filter(project__charity__id = my_id).order_by('-time_created')
        else:
            template_name_requests = 'requests_developer_content.html'
            requests    = Request.objects.filter(sender__id = my_id).order_by('-time_created')
        
        context = {}
        context['template_name_requests'] = template_name_requests
        context['params'] = kwargs
        context['requests'] = requests
        return context

class NotificationDetailView(LoginRequiredMixin, CorrectUserMixin, TemplateView):

    template_name       = 'notification_details.html'
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
            'params':   kwargs,
            'notification':  notification,
        }

def remove_developer(request, dev_id, proj_id):

    if not request.user.is_authenticated():
        return redirect(reverse_lazy('login'))

    project             = Project.objects.get(id=proj_id)
    to_be_removed       = User.objects.get(id=dev_id).get_profile()
    project_developers  = list(project.developers.all())
    project_developers.remove(to_be_removed)
    project.developers  = project_developers
    
    if request.user.id != project.charity.id:
        result =    {
                    'error_message': 'Something went wrong, this project belongs to user '+project.charity.company_name, 
                    'tr_id': '',
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        project.save()
        tr_id = "#developer-" + str(dev_id)
        result = {
                    'error_message': 'no_errors',
                    'tr_id': tr_id,
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def respond_to_request(request, pk, status):
    '''
    Accepts a Developer's request to help on a project
    and creates a notification to the Developer.
    '''
    if not request.user.is_authenticated():
        return redirect(reverse_lazy('login'))

    request_id          = pk
    my_request          = Request.objects.get(id=request_id)
    project             = my_request.project
    project_developers  = project.developers.all()
    project_owner       = my_request.project.charity
    request_sender      = my_request.sender

    if request.user.id != project_owner.id:
        result =    {
                    'error_message': 'Something went wrong, this project belongs to user '+project_owner.user.username, 
                    'status': '' 
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        my_request.status   = status
        my_request.save()
        if status == 'accepted':
            already_in = request_sender in project_developers
            if already_in:
                pass
            else:
                dev_list                = list(project_developers)
                dev_list.append(request_sender)
                project.developers      = dev_list
                # import pdb
                # pdb.set_trace()
                project.save()

        div_id = 'status-'+str(my_request.id)
        notification        = RequestNotification.objects.create(
                sender      = project_owner,
                receiver    = my_request.sender,
                request     = my_request,
                seen        = False,
            ) 
        result =    {
                    'div_id': div_id,
                    'status': status,
                    'error_message': '',
                    }
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

class NotificationsListView(LoginRequiredMixin, CorrectUserMixin, TemplateView):

    error_message = 'Oops, something went wrong. \
                    The browser was trying to access someone else\'s notification list.'
    def get_context_data(self, **kwargs):
        my_id           = self.request.user.id
        user_type       = self.request.user.get_profile().user_type

        if user_type == 'Developer':
            self.template_name  = 'my_notifications_developer.html'
            notifications       = RequestNotification.objects.filter(receiver__id = my_id, seen=False).order_by('-time_created')
        else:
            self.template_name  = 'my_notifications_charity.html'
            notifications       = RequestNotification.objects.filter(receiver__id = my_id, seen=False).order_by('-time_created')

        # needed for correct user mixin
        self.url_id            = self.kwargs['pk']
        return {
            'params':   kwargs,
            'notifications': notifications,
        }

def get_notifications(request, param):
    
    if not request.user.is_authenticated():
        return redirect(reverse_lazy('login'))

    if request.method == 'GET':
        my_id       = request.user.id

        if param == 'new':
            notifications = RequestNotification.objects.\
            filter(receiver__id = my_id, seen=False).order_by('-time_created')
        else:
            notifications = RequestNotification.objects.\
            filter(receiver__id = my_id).order_by('-time_created')      
        context = {}
        context['notifications'] = notifications

        user_type = request.user.get_profile().user_type
        # import pdb; 
        # pdb.set_trace()
        if user_type == 'Developer':
            return render_to_response('get_notifications_developer.html', context)
        else:
            return render_to_response('get_notifications_charity.html', context)

def get_requests(request, param):
    
    if not request.user.is_authenticated():
        return redirect(reverse_lazy('login'))
        
    if request.method == 'GET':
        my_id       = request.user.id
        user_type   = request.user.get_profile().user_type

        if user_type == 'Developer':
            id_kw   = 'sender__id'
            template_name = 'requests_developer_content.html'
        else:
            id_kw   = 'project__charity__id'
            template_name = 'requests_charity_content.html'

        status = param
        kwargs = {
            id_kw: str(my_id),
        }

        if param != 'all':
            kwargs.update({'status': status,})

        requests = Request.objects.\
            filter(**kwargs).order_by('-time_created')
        # import pdb; 
        # pdb.set_trace()

        context = {}
        context['requests'] = requests

        return render_to_response(template_name, context)

def notification_seen(request, pk):
    if not request.user.is_authenticated():
        return redirect(reverse_lazy('login'))

    notification        = RequestNotification.objects.get(id=pk)
    notification.seen   = True
    notification.save()
    result              = {'noti_id': pk}
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')