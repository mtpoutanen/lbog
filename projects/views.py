from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView, UpdateView
from projects.forms import ProjectCreationForm, ProjectChangeForm
from projects.models import Project
from django import forms
from django.utils import simplejson
from django.core.urlresolvers import reverse_lazy


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
        form.save()

        return super(ProjectCreationView, self).form_valid(form)

class ProjectCreatedView(UpdateView):
    template_name   = 'project-created.html'

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model           = Project
    login_url       = reverse_lazy('login-required')
    template_name   = 'change-project-details.html'
    form_class      = ProjectChangeForm
    success_url     = reverse_lazy('profile-changed')

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """ 
        super(ProjectUpdateView, self).get_initial()
        project_id      = self.kwargs['pk']
        project         = Project.objects.get(pk=project_id) 
        skill_list      = project.skills
        initial = {
            'skills':     list(skill_list.all()),
        }
        return initial

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response with a template rendered with the given context.
        """
        project             = Project.objects.get(id=kwargs['pk'])
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
            return self.response_class(
                request = self.request,
                template = 'wrong_project.html',
                context = context,
                **response_kwargs
            )

def charity_data(request):
    result = []
    profile = request.user.get_profile()
    result.append({
            'country': profile.country,
            'state': profile.country,
            'city': profile.city,
        })
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')