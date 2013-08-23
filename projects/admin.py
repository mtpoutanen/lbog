from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from projects.models import Project, HelpOffer, Notification

# Define an inline admin descriptor for Employee model

class TimeAdmin(admin.ModelAdmin):
	readonly_fields = ['time_created',]

admin.site.register(Project, TimeAdmin)
admin.site.register(HelpOffer, TimeAdmin)
admin.site.register(Notification)
