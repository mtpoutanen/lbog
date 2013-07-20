from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from projects.models import Project, Request

# Define an inline admin descriptor for Employee model
admin.site.register(Project)
admin.site.register(Request)
