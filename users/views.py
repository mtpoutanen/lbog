# Create your views here.

from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm, UserChangeForm
from users.forms import BaseCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from users.models import UserProfile

# def handle_uploaded_file(file):
#     destination = open('/images/test/testimage.jpg', 'wb+')
#     for chunk in f.chunks():
#         destination.write(chunk)
#     destination.close()

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/account/logged-in/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

class LoginSuccessfulView(TemplateView):
    # content_type = 'text/image'
    template_name = 'logged-in.html'

class RegistrationView(FormView):
    template_name = 'register.html'
    form_class = BaseCreationForm
    model = UserProfile
    success_url = '/account/login/'

    def form_valid(self, form):
        # form                    = BaseCreationForm(self.request.POST, self.request.FILES)
        user                    = form.save()
        profile                 = user.get_profile()
        profile.user_type       = form.cleaned_data['user_type']
        profile.title           = form.cleaned_data['title']
        profile.company_name    = form.cleaned_data['company_name']
        profile.country         = form.cleaned_data['country']
        profile.state           = form.cleaned_data['state']
        profile.city            = form.cleaned_data['city']
        profile.post_code       = form.cleaned_data['post_code']
        profile.address         = form.cleaned_data['address']
        profile.description     = form.cleaned_data['description']

        skill_list = []
        for skill in form.cleaned_data['skills']:
            skill_list.append(skill)
        profile.skills = skill_list

        profile.logo = form.cleaned_data['logo']

        profile.save()
        return super(RegistrationView, self).form_valid(form)