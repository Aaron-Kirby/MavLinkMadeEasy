from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import User, Course, Degree, Req, Prereq, Complete


#def selectdegree(request):
    #return render(request, 'landing/selectdegree.html')

'''
@login send a request to render the login.html page
@param request: generates the response
'''
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


'''
@selectcourses send a request to render the selectcourses.html page
@param request: generates the response
'''
def selectcourses(request):
    return render(request, 'landing/selectcourses.html')

'''
@schedule send a request to render the schedule.html page
@param request: generates the response
'''
def schedule(request):
    return render(request, 'landing/schedule.html')

'''
@createuser send a request to render the createuser.html page
@param request: generates the response
'''
def createuser(request):
    return render(request, 'landing/createuser.html')




