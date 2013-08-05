from django.db import models
from projects.models import get_image_path

# Create your models here.

class Story(models.Model):

	title 			= models.CharField(max_length=50, null=True, blank=True)
	article_body 	= models.TextField(null=True, blank=True)
	story_image 	= models.ImageField(upload_to=get_image_path, blank=True, null=True)
	time_created    = models.DateTimeField(auto_now_add=True, null=False, blank=False)

	def __unicode__(self):
		return self.title