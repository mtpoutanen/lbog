# Create your views here.

from braces.views import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, get_user_model
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView
from users.models import UserProfile
from users.forms import MyCreationForm, MyChangeForm
from projects.models import Project, Request
from projects.views import CorrectUserMixin
from django.http import HttpResponse
from django.utils import simplejson


def update_profile(user, form):
    profile                 = user.get_profile()
    profile.given_name      = form.cleaned_data['given_name']
    profile.family_name     = form.cleaned_data['family_name']
    profile.title           = form.cleaned_data['title']
    profile.company_name    = form.cleaned_data['company_name']
    profile.country         = form.cleaned_data['country']
    profile.state           = form.cleaned_data['state']
    profile.city            = form.cleaned_data['city']
    profile.lat             = form.cleaned_data['lat']
    profile.lon             = form.cleaned_data['lon']
    profile.description     = form.cleaned_data['description']
    profile.logo            = form.cleaned_data['logo']
    profile.www             = form.cleaned_data['www']
    profile.allow_contact   = form.cleaned_data['allow_contact']
    
    # only appears in the registration form
    if not user:
        profile.user_type       = form.cleaned_data['user_type']    

    skill_list = []
    for skill in form.cleaned_data['skills']:
        skill_list.append(skill)
    profile.skills          = skill_list
    profile.save()

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

class RegistrationView(FormView):
    model = UserProfile
    template_name = 'register.html'
    form_class = MyCreationForm
    success_url = reverse_lazy('registration-successful')

    def form_valid(self, form):
        user = form.save()
        update_profile(user, form)     
        return super(RegistrationView, self).form_valid(form)

    def render_to_response(self, context, **response_kwargs):

        """
        Returns a response with a template rendered with the given context.
        """

        if self.request.user.is_authenticated():
            self.template_name = 'already_logged_in.html'
            return self.response_class(
                request = self.request,
                template = self.get_template_names(),
                context = context,
                **response_kwargs
            )
        else:    
            return self.response_class(
                request = self.request,
                template = self.get_template_names(),
                context = context,
                **response_kwargs
            )

class PasswordChangeView(LoginRequiredMixin, CorrectUserMixin, FormView):
    form_class      = PasswordChangeForm
    # model           = User
    template_name   = 'registration/password_change_form.html'
    success_url     = reverse_lazy('profile-changed')

    # override to get login url
    def render_to_response(self, context, **response_kwargs):

        """
        Returns a response with a template rendered with the given context.
        """
        self.url_id = self.kwargs['pk']
        return self.response_class(
            request = self.request,
            template = self.get_template_names(),
            context = context,
            **response_kwargs
        )
    
class ChangeView(LoginRequiredMixin, CorrectUserMixin, UpdateView):

    model           = UserProfile  #get_user_model()
    login_url       = reverse_lazy('login')
    template_name   = 'change_account_details.html'
    form_class      = MyChangeForm
    success_url     = reverse_lazy('profile-changed')
    error_message   = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s profile.'
    
    def get_form(self, form_class):
        self.form_class         = MyChangeForm
        form = super(ChangeView, self).get_form(form_class)
        form.view_request       = self.request
        return form

    def form_valid(self, form):
        user = self.request.user
        update_profile(user, form)
        return super(ChangeView, self).form_valid(form)

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """ 
        super(ChangeView, self).get_initial()
        self.url_id = self.kwargs['pk']
        my_id       = self.kwargs['pk']
        my_user     = User.objects.get(pk=my_id) 
        profile     = my_user.get_profile()
        skill_list  = profile.skills
        initial = {
            'skills':     list(skill_list.all()),
        }
        return initial

class SuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'profile_change_done.html' 

class RegSuccessView(TemplateView):
    template_name = 'registration_done.html' 

class CharityView(TemplateView):

    template_name = 'charity_details.html'

    def get_context_data(self, **kwargs):
        charity_id      = kwargs['pk']
        charity         = UserProfile.objects.get(id = charity_id)
        return {
            'params':   kwargs,
            'charity':  charity,
        }

class DeveloperView(TemplateView):
    '''Displays the details of a Developer profile'''

    def get_context_data(self, **kwargs):
        dev_id          = kwargs['pk']
        developer     = UserProfile.objects.get(id = dev_id)
        return {
            'params':       kwargs,
            'developer':    developer,
        }    
    
    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response with a template rendered with the given context.
        """
        my_id                   = self.request.user.id
        developer               = context['developer']
        is_self                 = my_id == developer.id
        allow_contact           = developer.allow_contact
        dev_projects            = Project.objects.filter(developers__id__contains=developer.id)
        
        # check if the developer has sent requests to the charity
        charity_requests        = Request.objects.filter(sender=developer.id, project__charity__id=my_id)
        
        # check if the developer is assigned to any projects with the charity (largely redundant due to previous check)
        charity_projects        = filter(lambda project: 
                            project.charity.id == my_id, dev_projects)
        
        developer_permission    = []
        for project in dev_projects:
            # if a developer tries to access the profile, see if they are assigned to any common projects.
            developer_permission  = filter(lambda loop_developer: 
                            loop_developer.id == developer.id, project.developers.all())
        
        # import pdb
        # pdb.set_trace()
        
        if is_self or allow_contact or charity_requests or charity_projects or developer_permission:
            template = 'developer_details.html'
        else:
            template = 'no_developer_access.html'
        
        return self.response_class(
                request = self.request,
                template = template,
                context = context,
                **response_kwargs
            )


def deactivate_account(request):
    req_user = request.user
    if request.method == 'POST':
        req_user.is_active = False
        req_user.save()
        result = {
                'error_message': 'no_errors',
                }
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
