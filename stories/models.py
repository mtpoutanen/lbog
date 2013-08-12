from django.db import models
import os
# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('images/story_images', str(instance.id), filename)

class Story(models.Model):

	title 			= models.CharField(max_length=50, null=True, blank=True)
	article_body 	= models.TextField(null=True, blank=True)
	image 			= models.ImageField(upload_to=get_image_path, blank=True, null=True)
	time_created    = models.DateTimeField(auto_now_add=True, null=False, blank=False)

	def __unicode__(self):
		return self.title