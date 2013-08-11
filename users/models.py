from django.conf import settings
import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from users.models import *

def get_image_path(instance, filename):
    return os.path.join('images/profile_images', str(instance.id), filename)

class Skill(models.Model):
    """Skills and developers have a many-to-many relationship. Skills also used in projects"""
    skill_name      = models.CharField(max_length=50)

    def __unicode__(self):
        return self.skill_name

class Country(models.Model):
    country_name    = models.CharField(max_length=50)

    def __unicode__(self):
        return self.country_name

class State(models.Model):
    state_name    = models.CharField(max_length=50)

    def __unicode__(self):
        return self.state_name

class UserProfile(models.Model):
    '''
    Contains all the user information except for username, email and password 
    which are handled by Django's User class. Instead each user profile is 
    attached to a user object. Because a profile is created and saved immediately
    after a User object is created, not null conditions cannot be enforced on 
    these fields or else the db will throw an exception 
    '''
    user            = models.OneToOneField(User)
    user_type       = models.CharField(max_length=30, choices={
                    ('Developer', 'Developer'),
                    ('Charity', 'Charity'),
                    }, blank=False, null=False)
    allow_contact   = models.BooleanField(null=False, blank=False)
    given_name      = models.CharField(max_length=30, blank=True)
    family_name     = models.CharField(max_length=50, blank=True)
    title           = models.CharField(max_length=254, blank=True)
    company_name    = models.CharField(max_length=50, blank=True, null=True)
    www             = models.CharField(max_length=50, blank=True)
    country         = models.ForeignKey(Country, blank=False, 
                        null=False, default=1)
    state           = models.ForeignKey(State, blank=False, 
                        null=False, default=1)
    city            = models.CharField(max_length=50, blank=False,
                        null=False, default="")
    # post_code       = models.CharField(max_length=10, blank=True)
    # address         = models.CharField(max_length=100, blank=True)
    lat             = models.FloatField(blank=False, null=False, default=0.0)
    lon             = models.FloatField(blank=False, null=False, default=0.0)
    description     = models.TextField(blank=True, max_length=1000)
    # The forms do not allow Charities to upload skills
    skills          = models.ManyToManyField(Skill, null=True, blank=True)
    logo            = models.ImageField( \
                    upload_to=get_image_path, blank=True, null=True)

    def __unicode__(self):
        return self.user.username


def create_profile_callback(sender, instance, **kwargs):
    profile, new = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile_callback, sender=User)

