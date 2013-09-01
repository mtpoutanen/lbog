from django.shortcuts import render_to_response
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.models import User
from projects.forms import ProjectCreationForm, ProjectChangeForm, HelpOfferForm
from projects.models import Project, HelpOffer, Notification
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django import forms
from django.utils import simplejson
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

class CorrectUserMixin(object):
    #default error message
    error_message = 'You are logged in as the wrong user. \
                                No detailed error message was provided'
    url_id       = 0 # default value

    def render_to_response(self, context, **response_kwargs):
        """Returns either the desired template or wrong_user.html."""
        logged_in_id        = self.request.user.id
        # if no url_id was set in the view, raise an error
        if self.url_id == 0:
            raise ImproperlyConfigured("url_id missing")
        # if the object belongs to the is logged in user, return template
        if logged_in_id == int(self.url_id):
            return self.response_class(
                request = self.request,
                template = self.get_template_names(),
                context = context,
                **response_kwargs
            )
        # otherwise, return wrong_user.html with a custom error message
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
    model           = HelpOffer
    template_name   = 'project_details.html'
    success_url     = reverse_lazy('help-offer-sent')
    
    def get_form(self, form_class):
        form_class              = HelpOfferForm
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
        context['already_offered']      = False
        context['completed_projects']   = Project.objects.filter(status='completed')
        context['projects_under_way']   = Project.objects.filter(status='under_way')
        context['looking_projects']     = Project.objects.filter(status='looking')

        if self.request.user.is_authenticated():
            my_id                           = self.request.user.id
            # using filter instead of get just in case someone creates a second request in admin etc.
            offered_help_for_this_project   = HelpOffer.objects.filter(sender__id=my_id, project=project)
            context['already_offered']      = offered_help_for_this_project

        return context
    
    def form_valid(self, form):
        'render nothing if not the right user'
        profile                 = self.request.user.get_profile()
        form.instance.sender    = profile
        project_id              = self.kwargs['pk']
        project                 = Project.objects.get(id=project_id)
        form.instance.project   = project
        help_offer              = form.save()
        notification            = Notification.objects.create(
                sender          = profile,
                receiver        = project.charity,
                help_offer      = help_offer,
                seen            = False,
            ) 
        return super(ProjectDetailView, self).form_valid(form)

class HelpOfferSentView(LoginRequiredMixin, TemplateView):
    template_name   = 'help_offer_sent.html'

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

class HelpOfferListView(LoginRequiredMixin, CorrectUserMixin, TemplateView):

    template_name       = 'my_help_offers.html'
    error_message       = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s request list.'
    def get_context_data(self, **kwargs):

        self.url_id     = self.kwargs['pk']
        my_id           = self.request.user.id
        
        if self.request.user.get_profile().user_type == 'Charity':
            template_name_help_offers = 'help_offers_charity_content.html'
            help_offers    = HelpOffer.objects.filter(project__charity__id = my_id).order_by('-time_created')
        else:
            template_name_help_offers = 'help_offers_developer_content.html'
            help_offers    = HelpOffer.objects.filter(sender__id = my_id).order_by('-time_created')
        
        context = {}
        context['template_name_help_offers'] = template_name_help_offers
        context['params'] = kwargs
        context['help_offers'] = help_offers
        return context

class NotificationDetailView(LoginRequiredMixin, CorrectUserMixin, TemplateView):

    template_name       = 'notification_details.html'
    error_message       = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s request.'

    def get_context_data(self, **kwargs):

        help_offer_id       = int(self.kwargs['pk'])
        noti_id             = int(self.kwargs['noti'])
        notification        = Notification.objects.get(id=noti_id)
        notification.seen   = True
        notification.save()
        help_offer          = HelpOffer.objects.get(id=help_offer_id)
        if self.request.user.get_profile().user_type == 'Charity':
            self.url_id     = help_offer.project.charity.id
        else:
            self.url_id     = help_offer.sender.id   

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

def respond_to_help_offer(request, pk, status):
    '''
    Accepts a Developer's request to help on a project
    and creates a notification to the Developer.
    '''
    if not request.user.is_authenticated():
        return redirect(reverse_lazy('login'))

    help_offer_id       = pk
    help_offer          = HelpOffer.objects.get(id=help_offer_id)
    project             = help_offer.project
    project_developers  = project.developers.all()
    project_owner       = help_offer.project.charity
    help_offer_sender      = help_offer.sender

    if request.user.id != project_owner.id:
        result =    {
                    'error_message': 'Something went wrong, this project belongs to user '+project_owner.user.username, 
                    'status': '' 
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        help_offer.status   = status
        help_offer.save()
        if status == 'accepted':
            already_in = help_offer_sender in project_developers
            if already_in:
                pass
            else:
                dev_list                = list(project_developers)
                dev_list.append(help_offer_sender)
                project.developers      = dev_list
                # import pdb
                # pdb.set_trace()
                project.save()

        div_id = 'status-'+str(help_offer.id)
        notification        = Notification.objects.create(
                sender      = project_owner,
                receiver    = help_offer.sender,
                help_offer  = help_offer,
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
            notifications       = Notification.objects.filter(receiver__id = my_id, seen=False).order_by('-time_created')
        else:
            self.template_name  = 'my_notifications_charity.html'
            notifications       = Notification.objects.filter(receiver__id = my_id, seen=False).order_by('-time_created')

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
            notifications = Notification.objects.\
            filter(receiver__id = my_id, seen=False).order_by('-time_created')
        else:
            notifications = Notification.objects.\
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

def get_help_offers(request, param):
    
    if not request.user.is_authenticated():
        return redirect(reverse_lazy('login'))
        
    if request.method == 'GET':
        my_id       = request.user.id
        user_type   = request.user.get_profile().user_type

        if user_type == 'Developer':
            id_kw   = 'sender__id'
            template_name = 'help_offers_developer_content.html'
        else:
            id_kw   = 'project__charity__id'
            template_name = 'help_offers_charity_content.html'

        status = param
        kwargs = {
            id_kw: str(my_id),
        }

        if param != 'all':
            kwargs.update({'status': status,})

        help_offers = HelpOffer.objects.\
            filter(**kwargs).order_by('-time_created')
        # import pdb; 
        # pdb.set_trace()

        context = {}
        context['help_offers'] = help_offers

        return render_to_response(template_name, context)

def notification_seen(request, pk):
    if not request.user.is_authenticated():
        return redirect(reverse_lazy('login'))

    notification        = Notification.objects.get(id=pk)
    notification.seen   = True
    notification.save()
    result              = {'noti_id': pk}
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.user.id != project.charity.id:
        result =    {
                    'error_message': 'Something went wrong, this project belongs to user '+project.charity.company_name, 
                    'div_id': '',
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    elif project.status == 'completed':
        result =    {
                    'error_message': 'Sorry, cannot delete completed projects, please contact admin if this is necessary', 
                    'div_id': '',
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        if request.method == 'POST':
            project.delete()
            div_id = "#project-" + str(pk)
            result = {
                    'error_message': 'no_errors',
                    'div_id': div_id,
                    }
            return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def delete_notification(request, pk):
    ''' Deletes a notification '''

    # Get the notification to be deleted.
    notification = Notification.objects.get(id=pk)

    # Check if the URL is being called by the owner of that Notification
    if request.user.id != notification.receiver.id:
        # if not, return an error message
        result =    {
                    'error_message': 'Something went wrong, this notification belongs to user '+notification.receiver.user.username, 
                    'div_id': '',
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        # if yes, delete the notification and return a response with no error message.
        if request.method == 'POST':
            notification.delete()
            div_id = "#notification-" + str(pk)
            result = {
                    'error_message': 'no_errors',
                    'div_id': div_id,
                    }
            return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def delete_help_offer(request, pk):
    help_offer = HelpOffer.objects.get(id=pk)
    user_type = request.user.get_profile().user_type

    if not (
            (user_type == 'Developer'
            and request.user.id == help_offer.sender.id  
            ) 
        or 
        (   user_type == 'Charity'
            and request.user.id == help_offer.project.charity.id
            )
        ):
        result =    {
                    'error_message': 'Something went wrong, this request belongs to another user', 
                    'div_id': '',
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    elif help_offer.status == 'pending' and user_type == 'Charity':
        result =    {
                    'error_message': 'Please respond to the request before deleting.', 
                    'div_id': '',
                    }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        if request.method == 'POST':
            help_offer.delete()
            div_id = "#help-offer-" + str(pk)
            result = {
                    'error_message': 'no_errors',
                    'div_id': div_id,
                    }
            return HttpResponse(simplejson.dumps(result), mimetype='application/json')

