from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from stories.models import Story

# Define an inline admin descriptor for Employee model
admin.site.register(Story)