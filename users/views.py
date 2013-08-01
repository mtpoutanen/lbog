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
from projects.models import Project
from projects.views import CorrectUserMixin

def update_profile(user, form):
    profile                 = user.get_profile()
    profile.user_type       = form.cleaned_data['user_type']
    profile.title           = form.cleaned_data['title']
    profile.company_name    = form.cleaned_data['company_name']
    profile.country         = form.cleaned_data['country']
    profile.state           = form.cleaned_data['state']
    profile.city            = form.cleaned_data['city']
    profile.lat             = form.cleaned_data['lat']
    profile.lon             = form.cleaned_data['lon']
    profile.description     = form.cleaned_data['description']
    profile.logo            = form.cleaned_data['logo']

    skill_list = []
    for skill in form.cleaned_data['skills']:
        skill_list.append(skill)
    profile.skills          = skill_list
    profile.save()


class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('logged-in')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LoginRequiredView(TemplateView):
    template_name = 'login-required.html'


class LoginSuccessfulView(TemplateView):
    # content_type = 'text/image'
    template_name = 'logged-in.html'


class RegistrationView(FormView):
    model = UserProfile
    template_name = 'register.html'
    form_class = MyCreationForm
    success_url = reverse_lazy('registration-successful')

    def form_valid(self, form):
        user = form.save()
        update_profile(user, form)     
        return super(RegistrationView, self).form_valid(form)


class PasswordChangeView(FormView):
    form_class      = PasswordChangeForm
    # model           = User
    template_name   = 'registration/password_change_form.html'
    success_url     = reverse_lazy('profile-changed')
    

class ChangeView(LoginRequiredMixin, CorrectUserMixin, UpdateView):

    model           = UserProfile  #get_user_model()
    login_url       = reverse_lazy('login-required')
    template_name   = 'change-details.html'
    form_class      = MyChangeForm
    success_url     = reverse_lazy('profile-changed')
    error_message   = 'Oops, something went wrong. \
            The browser was trying to access someone else\'s profile.'

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

    template_name = 'charity-details.html'

    def get_context_data(self, **kwargs):
        charity_id      = kwargs['pk']
        charity         = UserProfile.objects.get(id = charity_id)
        return {
            'params':   kwargs,
            'charity':  charity,
        }
