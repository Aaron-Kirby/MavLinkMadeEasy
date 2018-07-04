from django.db import models
#from django.contrib.postgres.fields import ArrayField #this element is specific to postgres

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=75)
    major = models.CharField(max_length=75)
    degreetrack = models.CharField(max_length=75)
    classtaken = models.CharField(max_length=75)
    #classes_taken = ArrayField(
    #    models.CharField(max_length=75)
    #)
    def __str__(self):
        return self.email

class DegreePath(models.Model):
    major = models.CharField(max_length=75)
    degreetrack = models.CharField(max_length=75)
    course_name = models.CharField(max_length=75)
    def __str__(self):
        return self.major

class Courses(models.Model):
    course_name = models.CharField(max_length=75)
    course_number = models.CharField(max_length=75)
    prerequisite = models.CharField(max_length=75)
    #prereqs = ArrayField(
    #    models.CharField(max_length=75)
    #)
    def __str__(self):
        return self.course_name