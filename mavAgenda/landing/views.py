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

def getDegree(d, m):
    degreeTable = Degree.objects.all()
    for deg in degreeTable:
        if deg.major == m and deg.degree == d:
            return deg

# new createuser
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
            return HttpResponse(reverse('landing/selectcourses.html', userID))

    else:
        emailForm = EmailForm(prefix="e")
        degreeForm = DegreeForm(prefix="d")
    return render(request, 'landing/createuser.html', {'emailForm': emailForm, 'degreeForm':degreeForm})



