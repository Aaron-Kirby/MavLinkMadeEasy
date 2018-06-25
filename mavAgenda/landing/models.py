# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=75)
    major = models.CharField(max_length=75)
    track = models.CharField(max_length=75)
    degree = models.CharField(max_length=75)
    classes_taken = ArrayField(
        models.CharField(max_length=75)
    )

class DegreePath(models.Model):
    major = models.CharField(max_length=75)
    track = models.CharField(max_length=75)
    degree = models.CharField(max_length=75)
    course_name = models.CharField(max_length=75)

class Courses(models.Model):
    course_name = models.CharField(max_length=75)
    course_number = models.CharField(max_length=75)
    prereqs = ArrayField(
        models.CharField(max_length=75)
    )
