"""
Tests for the users application.
"""
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse_lazy
from users.models import * #will need every model

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

	FIELD_LIST = ['username', 'password', 'email', 'user_type',
	'given_name', 'family_name', 'title', 'company_name',
	'country', 'state', 'city', 'skills', 'description', 'lat', 'lon',
	]

	DEFAULT_VALUES = ['test_username', 'test_password', 'test_email@test.com', 'Developer', 
		'John', 'Default', 'Software Engineer', 'UCL', 'Finland', 
		'California', 'Mountain View',
		['Android', 'Java'], 
		'This is a test description', 30.0, 30.0,
	]

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

		return has_errors

	def test_create_user(self):
		has_errors = self.save_user(self.DEFAULT_VALUES)
		self.assertEqual(has_errors, False)

	def test_no_user_type(self):
		my_values = list(self.DEFAULT_VALUES)
		my_values[self.USER_TYPE] = 'something'
		has_errors = self.save_user(my_values) 
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

	def test_no_lat(self):
		my_values = list(self.DEFAULT_VALUES)
		my_values[self.LAT] = None
		has_errors = self.save_user(my_values) 
		self.assertEqual(has_errors, True)

	def test_no_lon(self):
		my_values = list(self.DEFAULT_VALUES)
		my_values[self.LON] = None
		has_errors = self.save_user(my_values) 
		self.assertEqual(has_errors, True)	

	def test_login(self):
		self.save_user(self.DEFAULT_VALUES)
		c = Client()
		response = c.post(reverse_lazy('login'), {'username': 'test_username', 'password': 'test_password'})
		self.assertEqual(response.status_code, 302)


	# def test_registration_form(self):
		
	# 	country 	= Country.objects.create(country_name = 'Finland')
		
	# 	state 		= State.objects.create(state_name = 'test state')
	# 	c = Client()
	# 	response = c.post(reverse_lazy('register'),
	# 		{'username': 'user',
	# 		'email': 'test@test.com',
	# 		'password1': 'password',
	# 		'password2': 'password',
	# 		'user_type': 'Developer',
	# 		'country': country,
	# 		'state': state,
	# 		'city': 'Vaasa',
	# 		'lat': 30.00,
	# 		'lon': 30.00,
	# 		})
	# 	self.assertEqual(response.status_code, 302)


