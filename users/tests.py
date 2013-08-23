"""
Tests for the users and projects application. The modularity of the
applications isn't quite what it should be and thus the apps are best
tested in a single file.
"""
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse_lazy
from users.models import * #will need every model
from projects.models import *
import datetime

class ModelTests(TestCase):

	USERNAME		= 0
	PASSWORD		= 1
	EMAIL			= 2
	USER_TYPE		= 3
	GIVEN_NAME		= 4
	FAMILY_NAME		= 5
	TITLE			= 6
	COMPANY_NAME	= 7
	COUNTRY			= 8
	STATE 			= 9
	CITY 			= 10
	SKILLS 			= 11
	DESCRIPTION		= 12
	LAT  			= 13
	LON 			= 14
	ALLOW_CONTACT 	= 15
	WWW 			= 16





	PROFILE_FIELD_LIST = ['username', 'password', 'email', 'user_type',
	'given_name', 'family_name', 'title', 'company_name',
	'country', 'state', 'city', 'skills', 'description', 'lat', 'lon',
	'allow_contact', 'www',
	]

	PROFILE_DEFAULT_VALUES = ['test_username', 'test_password', 'test_email@test.com', 'Developer', 
		'John', 'Default', 'Software Engineer', 'UCL', 'Finland', 
		'California', 'Mountain View',
		['Web Development Front End'], 
		'This is a test description', 30.0, 30.0, True, 'www.example.com'
	]

	P_TITLE = 0
	P_DESCRIPTION = 1
	P_SKILLS = 2
	P_STATUS = 3
	P_DEVELOPERS = 4
	P_CHARITY = 5
	P_NEED_LOCALS = 6
	P_COUNTRY = 7
	P_STATE = 8
	P_CITY = 9
	P_LAT = 10
	P_LON = 11
	P_TIME_CREATED = 12
	P_TIME_COMPLETED = 13
	
	PROJECT_DEFAULT_VALUES = ['test title', 'test descr', None, 'looking', None,
							None, True, 'United States', 'New York', 'New York City',
							0.0, 0.0, datetime.datetime.now(), None]

	R_SENDER = 0
	R_MESSAGE = 1
	R_PROJECT = 2
	R_TIME_CREATED = 3
	R_STATUS = 4

	N_HELP_OFFER = 0
	N_SENDER = 1
	N_RECEIVER = 2
	N_SEEN = 3
	N_TIME_CREATED = 4
	def save_user(self, values):
		user 					= User.objects.create()
		user.username 			= values[self.USERNAME]
		user.email 				= values[self.EMAIL]
		user.set_password(values[self.PASSWORD])
		user.save()

		profile 				= user.get_profile()
		profile.user_type 		= values[self.USER_TYPE]
		profile.given_name 		= values[self.GIVEN_NAME]
		profile.family_name 	= values[self.FAMILY_NAME]
		profile.title 			= values[self.TITLE]
		profile.company_name 	= values[self.COMPANY_NAME]
		country \
			= Country.objects.create(country_name=values[self.COUNTRY])
		country.save()
		profile.country 		= country
		state \
			= State.objects.create(state_name=values[self.STATE])
		state.save()
		profile.state 			= state
		profile.city 			= values[self.CITY]
		profile.lat 			= values[self.LAT]
		profile.lon 			= values[self.LON]
		profile.allow_contact 	= values[self.ALLOW_CONTACT]
		profile.www 			= values[self.WWW]
		
		skill_list 				= []
		for skill in values[self.SKILLS]:
			my_skill = Skill.objects.create(skill_name=skill)
			skill_list.append(my_skill)
		profile.skills 			= skill_list

		profile.description 	= values[self.DESCRIPTION]

		has_errors = False
		try:
			profile.full_clean()
		except ValidationError:
			has_errors = True

		try:
			profile.save()
		except IntegrityError:
			has_errors = True

		if has_errors:
			return None, has_errors
		else:
			return profile, has_errors

	def save_project(self, values):
		project 			= Project()
		project.title 		= values[self.P_TITLE]
		project.description = values[self.P_DESCRIPTION]
		project.status 		= values[self.P_STATUS]
		project.need_locals = values[self.P_NEED_LOCALS]
		project.city 		= values[self.P_CITY]
		project.lat 		= values[self.P_LAT]
		project.lon  		= values[self.P_LON]
		project.charity 	= values[self.P_CHARITY]
		project.time_created= values[self.P_TIME_CREATED]

		country 			= Country.objects.create(country_name=values[self.P_COUNTRY])
		country.save()
		project.country 	= country

		state 				= State.objects.create(state_name=values[self.P_STATE])
		state.save()
		project.state 		= state

		has_errors = False
		try:
			project.full_clean()
		except ValidationError:
			has_errors = True

		try:
			project.save()
		except IntegrityError:
			has_errors = True

		if has_errors:
			return None, has_errors
		else:
			return project, has_errors

	def test_create_user(self):
		profile, has_errors = self.save_user(self.PROFILE_DEFAULT_VALUES)
		self.assertEqual(has_errors, False)

	def test_no_user_type(self):
		my_values = list(self.PROFILE_DEFAULT_VALUES)
		my_values[self.USER_TYPE] = 'something'
		profile, has_errors = self.save_user(my_values) 
		self.assertEqual(has_errors, True)

	def test_no_city(self):
		my_values = list(self.PROFILE_DEFAULT_VALUES)
		my_values[self.CITY] = ''
		profile, has_errors = self.save_user(my_values) 
		self.assertEqual(has_errors, True)

	def test_allow_contact(self):
		my_values = list(self.PROFILE_DEFAULT_VALUES)
		my_values[self.ALLOW_CONTACT] = None
		profile, has_errors = self.save_user(my_values) 
		self.assertEqual(has_errors, True)

	def test_no_lat(self):
		my_values = list(self.PROFILE_DEFAULT_VALUES)
		my_values[self.LAT] = None
		profile, has_errors = self.save_user(my_values) 
		self.assertEqual(has_errors, True)

	def test_no_lon(self):
		my_values = list(self.PROFILE_DEFAULT_VALUES)
		my_values[self.LON] = None
		profile, has_errors = self.save_user(my_values) 
		self.assertEqual(has_errors, True)	

	def test_no_country(self):
		my_values = list(self.PROFILE_DEFAULT_VALUES)
		my_values[self.COUNTRY] = None
		has_errors = False
		try:
			self.save_user(my_values) 
		except:
			has_errors = True
		self.assertEqual(has_errors, True)

	def test_no_state(self):
		my_values = list(self.PROFILE_DEFAULT_VALUES)
		my_values[self.STATE] = None
		has_errors = False
		try:
			self.save_user(my_values) 
		except:
			has_errors = True
		self.assertEqual(has_errors, True)

	def test_country_none(self):
		has_errors = False
		try:
			country = Country.objects.create(country_name = None)
		except IntegrityError:
			has_errors = True
		self.assertEqual(has_errors, True)

	def test_state_none(self):
		has_errors = False
		try:
			state = State.objects.create(state_name = None)
		except IntegrityError:
			has_errors = True
		self.assertEqual(has_errors, True)


	def test_login(self):
		self.save_user(self.PROFILE_DEFAULT_VALUES)
		c = Client()
		response = c.post(reverse_lazy('login'), {'username': 'test_username', 'password': 'test_password'})
		self.assertEqual(response.status_code, 302)

	def get_charity_profile(self):
		profile_values = list(self.PROFILE_DEFAULT_VALUES)
		profile_values[self.USER_TYPE] = 'Charity'
		profile, err = self.save_user(profile_values)
		project_values = list(self.PROJECT_DEFAULT_VALUES)
		project_values[self.P_CHARITY] = profile
		return profile, project_values

	def test_create_project(self):
		profile, project_values = self.get_charity_profile()
		project, has_errors = self.save_project(project_values)
		self.assertEqual(has_errors, False)

	def test_no_title(self):
		profile, project_values = self.get_charity_profile()
		project_values[self.P_TITLE] = ''
		project, has_errors = self.save_project(project_values)
		self.assertEqual(has_errors, True)

	def test_no_lat(self):
		profile, project_values = self.get_charity_profile()
		project_values[self.P_LAT] = None
		project, has_errors = self.save_project(project_values)
		self.assertEqual(has_errors, True)

	def test_no_lon(self):
		profile, project_values = self.get_charity_profile()
		project_values[self.P_LON] = None
		project, has_errors = self.save_project(project_values)
		self.assertEqual(has_errors, True)

	def test_no_status(self):
		profile, project_values = self.get_charity_profile()
		project_values[self.P_STATUS] = None
		project, has_errors = self.save_project(project_values)
		self.assertEqual(has_errors, True)

	def test_no_time_created(self):
		profile, project_values = self.get_charity_profile()
		project_values[self.P_STATUS] = None
		project, has_errors = self.save_project(project_values)
		self.assertEqual(has_errors, True)