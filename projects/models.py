from django.db import models
from users.models import Skill, UserProfile, Country, State
import os
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('images/project_images', str(instance.id), filename)

class Project(models.Model):

    STATUS_CHOICES = {
        ('looking', 'Looking for developers'),
        ('under_way', 'Project under way'),
        ('completed', 'Project completed'),
    }

    title           = models.CharField(max_length=50, blank=False, null=False)
    description     = models.TextField(blank=True)
    image           = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    skills          = models.ManyToManyField(Skill)
    status          = models.CharField(choices=STATUS_CHOICES, max_length=50,
                        blank=False, null=False, default='looking')
    # restrict to Developers at form level.
    developers      = models.ManyToManyField(UserProfile, related_name='project_developers',
                            null=True, blank=True)
    # restrict to Charities at form level
    charity         = models.ForeignKey(UserProfile, related_name='project_charity',
                                null=False, blank=False)
    need_locals     = models.BooleanField()
    country         = models.ForeignKey(Country, blank=False,
                        null=False)
    state           = models.ForeignKey(State, blank=False, 
                        null=False)
    city            = models.CharField(max_length=50, blank=False,
                        null=False)
    lat             = models.FloatField(blank=False, null=False, default=0.0)
    lon             = models.FloatField(blank=False, null=False, default=0.0)
    time_created    = models.DateTimeField(auto_now_add=True,
                        null=False, blank=False)
    time_completed  = models.DateTimeField(null=True, blank=True)


    def __unicode__(self):
        return self.title

class Request(models.Model):

    REQUEST_CHOICES = {
        ('pending', 'pending'),
        ('rejected', 'rejected'),
        ('accepted', 'accepted'),
    }
    # restrict to developers, validation at form level
    sender          = models.ForeignKey(UserProfile,
                        null=False, blank=False)
    message         = models.TextField(blank=True)
    project         = models.ForeignKey(Project,
                        null=False, blank=False)
    time_created    = models.DateTimeField(auto_now_add=True,
                        null=False, blank=False)
    status          = models.CharField(max_length=10, choices=REQUEST_CHOICES,
                        null=False, blank=False, default='pending')

    def __unicode__(self):
        return      "Request for " + self.project.title + " from " + self.sender.user.username

class RequestNotification(models.Model):
    request         = models.ForeignKey(Request) 
    sender          = models.ForeignKey(UserProfile,
                    null=False, blank=False, related_name="noti_sender")
    receiver        = models.ForeignKey(UserProfile,
                    null=False, blank=False, related_name="noti_receiver")
    seen            = models.BooleanField(null=False, blank=False,
                    default=False)
    time_created    = models.DateTimeField(auto_now_add=True,
                        null=False, blank=False)

    def __unicode__(self):
        return 'Notification for ' + self.request.project.title