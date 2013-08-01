# Create your views here.
from django.views.generic.detail import DetailView
from stories.models import Story

class StoryDetailView(DetailView):
	model       	= Story
	template_name   = 'story_details.html'

	def get_context_data(self, **kwargs):
		context = super(StoryDetailView, self).get_context_data(**kwargs)
		context['other_stories'] = Story.objects.all()
		return context