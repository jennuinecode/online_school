from __future__ import unicode_literals
from django.db import models
# from ..courses.models import Course

import re
import bcrypt

class StudentManager(models.Manager):

	def create_student(self, house, first, last, email, pw_hash):
		student = self.create(house=house,first_name=first, last_name=last, email=email, pw_hash=pw_hash)
		return student

	def hash_password(self, password):
		password = password.encode()
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
		return hashed_pw

	def login_check(self, data):
		errors=[]
		email = data['email']
		password = data['password'].encode()
		try:
			student = self.get(email=email)
			hashed_pw = student.pw_hash.encode()
			if bcrypt.hashpw(password, hashed_pw) == hashed_pw:
				return (True, student)
		except:
			errors.append("Incorrect email or password")

		return (False, errors)

	def validate_registration(self, data):
		errors = []
		first = data['first_name']
		last = data['last_name']
		email = data['email']
		password = data['password']

		if len(first) < 2:
			errors.append("Please enter a first name.")
		if len(last) < 2:
			errors.append("Please enter a last name.")
		if len(email) < 1:
			errors.append("Please enter an email address.")
		elif not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
			errors.append("Please enter a valid email address")
		if len(password) < 8:
			errors.append("Password must have atleast 8 characters")

		if not errors:
			try:
				matches = self.get(email=email)
				errors.append("A student already exists with that email.")
				return (False, errors)
			except:
				pw_hash = self.hash_password(data['password'])
				student = self.create_student(data['house'], data['first_name'], data['last_name'], data['email'], pw_hash)
				return (True, student)
		else:
			return (False, errors)


class Student(models.Model):
	house = models.CharField(max_length=100)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	# courses 
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = StudentManager()
