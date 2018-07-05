from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=75)
    degreetrack = models.CharField(max_length=75)
    major = models.CharField(max_length=75)
    classtaken = models.CharField(max_length=75)
    def __str__(self):
        return self.email

class UserCompleted(models.Model):
    user = models.IntegerField() # how to get the id from user as its own field
    coursenumber = models.CharField(max_length=75)
    def ___str___(self):
        return self.coursenumber

class PossibleDegrees(models.Model):
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=75)
    def ___str___(self):
        return self.degree + " in " + self.major


class RequirementCategories(models.Model):
    #how to get id
    core = models.IntegerField()
    corenumbercredits = models.IntegerField()
    english = models.IntegerField()
    englishnumbercredits = models.IntegerField()
    math = models.IntegerField()
    mathnumbercredits = models.IntegerField()
    speech = models.IntegerField()
    speechnumbercredits = models.IntegerField()
    # add as needed?
    def ___str___(self):
        return "yay!"

class Course(models.Model):
    coursename = models.CharField(max_length=75)
    coursenumber = models.CharField(max_length=75)
    semesteravailable = models.CharField(max_length=1) #A for all, S for spring, F for fall
    numbercredits = models.IntegerField()
    def ___str___(self):
        return self.coursenumber

class CoursePrereqs(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber



###########################3



class CoreCourse(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber

class EnglishCourse(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber

class MathCourse(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber

class SpeechCourse(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber