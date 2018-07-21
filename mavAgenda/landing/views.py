from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import *
from .forms import *

def getUserByEmail(e):
    userTable = User.objects.all()
    for cu in userTable:
        if cu.email == e:
            return cu

def getDegree(d, m):
    degreeTable = Degree.objects.all()
    for deg in degreeTable:
        if deg.major == m and deg.degree == d:
            return deg

#########################################

def login(request):
    if request.method == "POST":
        emailForm = EmailForm(request.POST, prefix = "e")
        if emailForm.is_valid():
            eF = emailForm.save(commit=False)
            u = getUserByEmail(eF.email)
            userID = u.id
            return HttpResponseRedirect(reverse('landing:selectcourses', args=(userID,)))
    else:
        emailForm = EmailForm(prefix="e")
    return render(request, 'landing/login.html', {'emailForm': emailForm, })

def selectcourses(request, pk):
    if request.method == "POST":
        form = UserCompletedForm(request.POST)
        if form.is_valid():

            # we want to delete everything from the UserCompleted table with the pk provided
            # then update to add the classes selected

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
        emailForm = EmailForm(request.POST, prefix = "e")
        degreeForm = DegreeForm( request.POST, prefix = "d")
        if emailForm.is_valid() and degreeForm.is_valid():
            dF = degreeForm.save(commit=False)
            eF = emailForm.save(commit=False)
            deg = getDegree(dF.degree, dF.major)
            u = User(email = eF.email, degree=deg)
            u.save()
            userID = u.id
            return HttpResponseRedirect(reverse('landing:selectcourses', args=(userID,)))
    else:
        emailForm = EmailForm(prefix="e")
        degreeForm = DegreeForm(prefix="d")
    return render(request, 'landing/createuser.html', {'emailForm': emailForm, 'degreeForm':degreeForm})