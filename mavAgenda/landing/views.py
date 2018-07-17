from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import User, Course, Degree, Req, Prereq, Complete

def login(request):
    return render(request, 'landing/login.html')

def selectcourses(request):
    return render(request, 'landing/selectcourses.html')

def schedule(request):
    return render(request, 'landing/schedule.html')

def createuser(request):
    return render(request, 'landing/createuser.html')




