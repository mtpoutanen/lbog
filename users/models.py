from django.conf import settings
import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
    user           = models.OneToOneField(User)
    user_type       = models.CharField(max_length=30, choices={
                    ('Developer', 'Developer'),
                    ('Charity', 'Charity'),
                    })
    title           = models.CharField(max_length=254, blank=True)
    company_name    = models.CharField(max_length=50, blank=True)
    country         = models.ForeignKey(Country, blank=True, null=True)
    state           = models.ForeignKey(State, blank=True, null=True)
    city            = models.CharField(max_length=50, blank=False, null=False)
    post_code       = models.CharField(max_length=10, blank=True)
    address         = models.CharField(max_length=100, blank=True)
    description     = models.TextField(blank=True)
    skills          = models.ManyToManyField(Skill)
    logo            = models.ImageField( \
                    upload_to=get_image_path, blank=True, null=True)

    def __unicode__(self):
        return self.user.username


def create_profile_callback(sender, instance, **kwargs):
    profile, new = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile_callback, sender=User)

