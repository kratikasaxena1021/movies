from django.db import models

# Create your models here.


# For database access from shell use this:
# from cms.models import
class Course(models.Model):

	name = models.CharField(max_length=50)
	course_fee = models.IntegerField(default=0)
	course_duration = models.IntegerField(default=0)

	course_tutor = models.IntegerField(blank=True, null=True)

	course_lang = models.CharField(max_length=2, blank=True, null=True)
class Student(models.Model):

	first = models.CharField(max_length=50)
	last = models.CharField(max_length=100)
	password = models.CharField(max_length=2, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)

	

