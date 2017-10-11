from django.db import models

# Create your models here.

class Course(models.Model):

	name = models.CharField(max_length=50)
	course_fee = models.IntegerField()
	course_duration = models.IntegerField()