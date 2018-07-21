from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import *
from .forms import *

def login(request):
    return render(request, 'landing/login.html')

def selectcourses(request, pk):
    if request.method == "POST":
        form = UserCompletedForm(request.POST)
        #assign pk number
        if form.is_valid():
            courses = form.save(commit=False)
            courses.save()
            return HttpResponseRedirect(reverse('landing:schedule'))
    else:
        form = UserCompletedForm()
    return render(request, 'landing/selectcourses.html', {'form': form})

def schedule(request):
    return render(request, 'landing/schedule.html')

def createuser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            degreeID = getDegreeID(form.degreeForm.degree, form.degreeForm.major)
            u = User( email = form.emailForm.email, degree=degreeID)
            u.save(commit=False)
            u.save()
            args = {'PK':u.id}
            #return render(request, 'landing/selectcourses.html', {'form': form})
            return HttpResponseRedirect(reverse('landing:selectcourses/'), args)
    else:
        form = UserForm()
    return render(request, 'landing/createuser.html', {'form': form})

def getDegreeID(d, m):
    for d in Degree:
        if d.major == m and d.degree == d:
            return d.id

