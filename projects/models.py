from django.db import models
from users.models import Skill, UserProfile, Country, State
import os
# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('images/project_images', str(instance.id), filename)


class Project(models.Model):
    ''' The main class of the application '''
    
    STATUS_CHOICES = {
        ('looking', 'Looking for developers'),
        ('under_way', 'Project under way'),
        ('completed', 'Project completed'),
    }

    title           = models.CharField(max_length=50, blank=False, null=False)
    description     = models.TextField(blank=True, max_length=1000)
    image           = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    skills          = models.ManyToManyField(Skill)
    status          = models.CharField(choices=STATUS_CHOICES, max_length=50,
                                    blank=False, null=False, default='looking')
    # Control at form level that only Developes can be added to Projects.
    developers      = models.ManyToManyField(UserProfile, related_name='project_developers',
                            null=True, blank=True)
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

    # The __unicode__ method defines the default description for the model
    def __unicode__(self):
        return self.title

class HelpOffer(models.Model):
    ''' HelpOffers can only be sent by Developers. This is controlled 
        at form validation and template rendering level '''

    HELP_OFFER_CHOICES = {
        ('pending', 'pending'),
        ('rejected', 'rejected'),
        ('accepted', 'accepted'),
    }

    sender          = models.ForeignKey(UserProfile,
                        null=False, blank=False)
    message         = models.TextField(blank=True)
    project         = models.ForeignKey(Project,
                        null=False, blank=False)
    time_created    = models.DateTimeField(auto_now_add=True,
                        null=False, blank=False)
    status          = models.CharField(max_length=10, choices=HELP_OFFER_CHOICES,
                        null=False, blank=False, default='pending')

    def __unicode__(self):
        return      "Help offer for " + self.project.title + " from " + self.sender.user.username

class Notification(models.Model):
    ''' Notifications are generated automatically when 
        a HelpOffer is sent or responded to '''

    help_offer      = models.ForeignKey(HelpOffer) 
    sender          = models.ForeignKey(UserProfile,
                    null=False, blank=False, related_name="noti_sender")
    receiver        = models.ForeignKey(UserProfile,
                    null=False, blank=False, related_name="noti_receiver")
    seen            = models.BooleanField(null=False, blank=False,
                    default=False)
    time_created    = models.DateTimeField(auto_now_add=True,
                        null=False, blank=False)

    def __unicode__(self):
        return 'Notification for ' + self.help_offer.project.title