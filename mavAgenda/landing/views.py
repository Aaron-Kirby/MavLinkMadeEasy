from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import *

import datetime

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

def getCompletedByUser(uID):
    cu = User.objects.get(pk=uID)
    completedCourses = []
    completedTable = Complete.objects.all()
    for c in completedTable:
        if c.user == cu:
            completedCourses.append(c)
    return completedCourses

def getCoursesForUser(uID):
    cu = User.objects.get(pk=uID)
    requiredCourses = []
    for cc in cu.degree.req.all():
        requiredCourses.append(cc)
    return requiredCourses

def removeCoursesTaken( requiredClasses, classesTaken ):
    validCourses = []
    for rc in requiredClasses:
        if rc not in classesTaken :
            validCourses.add(rc)
    return validCourses

def checkPrereqsMet(preqreqs, classesTaken, scheduledClasses):
    met = True
    for pr in preqreqs:
        if pr not in classesTaken and pr not in scheduledClasses:
            met = False
            break
    return met

def checkOfferedSemester(course, ssf):
    offered = False
    currentSem = "A"
    if ssf == "Spring":
        currentSem = "S"
    elif ssf == "Summer":
        currentSem = "M"
    else:
        currentSem = "F"
    if course.semester == currentSem or course.semester == 'A':
        offered = True
    return offered


def checkCourseValid(course, classesTaken, scheduledClasses, ssf):
    valid = False
    prereqs = course.prereqs
    prereqsMet = checkPrereqsMet(prereqs, classesTaken, scheduledClasses)
    offered = checkOfferedSemester(course, ssf)
    if prereqsMet and offered:
        valid = True
    return valid

def getSemesterByMonthYear( m ):
    if  m < 5 :
        title = "Spring"
    elif  m < 8 :
        title = "Summer"
    else:
        title = "Fall"
    return title

def generateNewSemester(semester):
    ssf = semester[0]
    y = semester[1]
    if ssf == "Spring" :
        ssf = "Summer"
    elif ssf == "Summer" :
        ssf = "Fall"
    else:
        ssf == "Spring"
        y += 1
    semester[0] = ssf
    semester[1] = y
    semester[2].clear()
    return semester

def isFull(courseList):
    full = False
    totalCredits = 0
    for c in courseList:
        totalCredits+= c.credits
    if totalCredits >= 12 and totalCredits <= 16:
        full = True
    return full

def createSchedule(uID):
    requiredClasses = getCoursesForUser(uID)
    classesTaken = User.objects.get(user_id = uID)
    neededClasses = removeCoursesTaken( requiredClasses, classesTaken )
    schedule = []
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    ssfSemester = getSemesterByMonthYear(currentMonth)
    semesterCourses = []
    semester = (ssfSemester, currentYear, semesterCourses)
    currentSemester = generateNewSemester(semester)
    for nc in neededClasses:
        if ( checkCourseValid( nc, classesTaken, schedule, ssfSemester ) ):
            currentSemester[1].add(nc)
            neededClasses.remove(nc)
        if ( neededClasses != [] and isFull(semester[2])):
            schedule.add(semester)
            semester = generateNewSemester(semester)
    return schedule

def emailFound(email):
    found = False
    userTable = User.objects.all()
    for cu in userTable:
        if cu.email == email:
            found = True
    return found

#########################################

def login(request):
    if request.method == "POST":
        emailForm = EmailForm(request.POST, prefix = "e")
        if emailForm.is_valid():
            eF = emailForm.save(commit=False)
            if emailFound(eF.email):
                u = getUserByEmail(eF.email)
                userID = u.id
                return HttpResponseRedirect(reverse('landing:schedule', args=(userID,)))
            else:
                emailForm = EmailForm(prefix="e")
                message = "Email not found"
                return render(request, 'landing/login.html', {'emailForm': emailForm, 'message':message})
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
            return HttpResponseRedirect(reverse('landing:schedule', args=(pk,)))
    else:
        form = UserCompletedForm()
    return render(request, 'landing/selectcourses.html', {'form': form})

def schedule(request, pk):
    return render(request, 'landing/schedule.html')

def createuser(request):
    if request.method == "POST":
        emailForm = EmailForm(request.POST, prefix = "e")
        degreeForm = DegreeForm( request.POST, prefix = "d")
        if emailForm.is_valid() and degreeForm.is_valid():
            dF = degreeForm.save(commit=False)
            eF = emailForm.save(commit=False)
            deg = getDegree(dF.degree, dF.major)
            if emailFound(eF.email):
                message = "Email already active"
                emailForm = EmailForm(prefix="e")
                degreeForm = DegreeForm(prefix="d")
                return render(request, 'landing/createuser.html', {'emailForm': emailForm, 'degreeForm':degreeForm, 'message': message})
            else:
                u = User(email = eF.email, degree=deg)
                u.save()
                userID = u.id
                return HttpResponseRedirect(reverse('landing:selectcourses', args=(userID,)))
    else:
        emailForm = EmailForm(prefix="e")
        degreeForm = DegreeForm(prefix="d")
    return render(request, 'landing/createuser.html', {'emailForm': emailForm, 'degreeForm':degreeForm})