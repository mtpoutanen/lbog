# Create your views here.
from django.views.generic import TemplateView
from stories.models import Story

class StoryDetailView(TemplateView):
	model       	= Story
	template_name   = 'story_details.html'

	def get_context_data(self, **kwargs):
		story_id = kwargs['pk']
		context = super(StoryDetailView, self).get_context_data(**kwargs)
		context['story'] 			= Story.objects.get(id=story_id)
		context['other_stories'] 	= Story.objects.all()
		return context