from django.db import models
from users.models import Skill, UserProfile, Country, State
import os
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('images/project_images', str(instance.id), filename)

class Project(models.Model):

	STATUS_CHOICES = {
		('looking', 'looking'),
		('under_way', 'under_way'),
		('completed', 'completed'),
	}

	title 			= models.CharField(max_length=50, blank=False, null=False)
	description 	= models.TextField(blank=True)
	image 			= models.ImageField(upload_to=get_image_path, blank=True, null=True)
	skills_needed	= models.ManyToManyField(Skill)
	status 			= models.CharField(choices=STATUS_CHOICES, max_length=50)
	# restrict to Developers at form level.
	developers 		= models.ManyToManyField(UserProfile, related_name='project_developers',
							null=True, blank=True)
	# restrict to Charities at form level
	charity 		= models.ForeignKey(UserProfile, related_name='project_charity',
								null=False, blank=False)
	need_locals 	= models.BooleanField()
	country         = models.ForeignKey(Country, blank=False,
						null=False)
	state           = models.ForeignKey(State, blank=False, 
						null=False)
	city            = models.CharField(max_length=50, blank=False,
                        null=False)
	lat             = models.FloatField(blank=False, null=False, default=0.0)
	lon             = models.FloatField(blank=False, null=False, default=0.0)

	def __unicode__(self):
		return self.title

class Request(models.Model):

	REQUEST_CHOICES = {
		'pending': 'pending',
		'rejected': 'rejected',
		'accepted': 'accepted',
	}
	# restrict to developers, validation at form level
	sender 			= models.ForeignKey(UserProfile)
	message 		= models.TextField(blank=True)
	project 		= models.ForeignKey(Project)
