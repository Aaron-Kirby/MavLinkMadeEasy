from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import User
from .models import UserCompleted
from .models import PossibleDegrees
from .models import RequirementCategories
from .models import Course
from .models import CoursePrereqs
from .models import CoreCourse
from .models import EnglishCourse
from .models import MathCourse
from .models import SpeechCourse

#def selectdegree(request):
    #return render(request, 'landing/selectdegree.html')

def login(request):
    return render(request, 'landing/login.html')
#def get_email(request):
    # if this is a POST request we need to process the form data
    #if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = LoginForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/schedule/')

    # if a GET (or any other method) we'll create a blank form
    #else:
        #form = LoginForm()


def selectcourses(request):
    return render(request, 'landing/selectcourses.html')


def schedule(request):
    return render(request, 'landing/schedule.html')


def createuser(request):
    return render(request, 'landing/createuser.html')








