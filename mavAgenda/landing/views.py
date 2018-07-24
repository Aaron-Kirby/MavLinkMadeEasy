from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import *

import datetime

'''
@getUserByEmail searches the User table to find the User object with a corresponding email
@param e: the email being searched for
'''
def getUserByEmail(e):
    userTable = User.objects.all()
    for cu in userTable:
        if cu.email == e:
            return cu

'''
@getDegree searches the Degree table to find the Degree object with corresponding degree and major
@param d: degree attribute of Degree being searched for
@param m: major attribute of Degree being searched for
'''
def getDegree(d, m):
    degreeTable = Degree.objects.all()
    for deg in degreeTable:
        if deg.major == m and deg.degree == d:
            return deg

'''
@getCompletedByUser provides a list of Course (objects) the user has taken
@param uID: the primary key corresponding to the active user
'''
def getCompletedByUser(uID):
    cu = User.objects.get(pk=uID)
    completedCourses = []
    completedTable = Complete.objects.all()
    for c in completedTable:
        if c.user == cu:
            completedCourses.append(c)
    return completedCourses

'''
@getCoursesForUser provides a list of Course (objects) the user must complete for their respective Degree
@param uID: the primary key corresponding to the active user
'''
def getCoursesForUser(uID):
    cu = User.objects.get(pk=uID)
    requiredCourses = []
    for cc in cu.degree.req.all():
        requiredCourses.append(cc)
    return requiredCourses

'''
@removeCoursesTaken provides a list of Course (objects) the user must still take (required, but not completed classes)
@param requiredClasses: a list of Course (objects) required for the User's Degree
@param classesTaken: a list of Course (objects) that the User has already completed
'''
def removeCoursesTaken( requiredClasses, classesTaken ):
    validCourses = []
    for rc in requiredClasses:
        if rc not in classesTaken :
            validCourses.add(rc)
    return validCourses

'''
@checkPrereqsMet determines if the User has met all Prereqs for a particular Course
@param prereqs: a list of Course (objects) corresponding to Prereqs for a given Course
@param classesTaken: a list of Course (objects) that the User has already completed
@parm scheduledClasses: a list of Course (objects) the scheduling algorithm has accounted for already
'''
def checkPrereqsMet(preqreqs, classesTaken, scheduledClasses):
    met = True
    for pr in preqreqs:
        if pr not in classesTaken and pr not in scheduledClasses:
            met = False
            break
    return met

'''
@checkOfferedSemester determines if a given Course if offered during the current semester
@param course: the Course under test
@param ssf: the Spring, Summer, Fall, offering attribute of the Course
'''
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

'''
@checkCourseValid determines if a given Course can be taken during a given semester
@param course: the Course under test
@param classesTaken: a list of Course (objects) that the User has already completed
@parm scheduledClasses: a list of Course (objects) the scheduling algorithm has accounted for already
@param ssf: the Spring, Summer, Fall, offering attribute of the Course
'''
def checkCourseValid(course, classesTaken, scheduledClasses, ssf):
    valid = False
    prereqs = course.prereqs
    prereqsMet = checkPrereqsMet(prereqs, classesTaken, scheduledClasses)
    offered = checkOfferedSemester(course, ssf)
    if prereqsMet and offered:
        valid = True
    return valid

'''
@getSemesterByMonthYear determines semester (Spring, Summer, Fall) according to current month
@param m: current month
'''
def getSemesterByMonthYear( m ):
    if  m < 5 :
        title = "Spring"
    elif  m < 8 :
        title = "Summer"
    else:
        title = "Fall"
    return title

'''
@generateNewSemester creates a new logical semester
@param semester: previous semester list
'''
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

'''
@isFull determines if a semester has hit the maximum number of credits allowable
@param courseList: list of Course (objects) the user is scheduled to take during current semester
'''
def isFull(courseList):
    full = False
    totalCredits = 0
    for c in courseList:
        totalCredits+= c.credits
    if totalCredits >= 12 and totalCredits <= 16:
        full = True
    return full

'''
@createSchedule generates semester-by-semester schedule for User's needed Courses according to Degree
@param uID: primary key associated with active user
'''
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

'''
@generateCheckBoxEntities creates a list of tuples of course name and number for the selectcourses page
@param uID: primary key corresponding to the active user
'''
def generateCheckBoxEntities(uID):
    courseList = getCompletedByUser(uID)
    checkBoxEntities = []
    for c in courseList:
        pair = (c.num, c.name)
        checkBoxEntities.add(pair)
    return checkBoxEntities

'''
@emailFound provides feedback if the email is already in the User database table
@param email: email under test
'''
def emailFound(email):
    found = False
    userTable = User.objects.all()
    for cu in userTable:
        if cu.email == email:
            found = True
    return found

########################################################################################################################
########################################################################################################################

'''
@login send a request to render the login.html page
@param request: generates the response
'''
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

'''
@selectcourses send a request to render the selectcourses.html page
@param request: generates the response
@param pk: primary key corresponding to active user
'''
def selectcourses(request, pk):
    if request.method == "POST":
        #form = UserCompletedForm(request.POST)
        #if form.is_valid():

            # we want to delete everything from the UserCompleted table with the pk provided
            # then update to add the classes selected

            #courses = form.save(commit=False)
            #courses.save()
            return HttpResponseRedirect(reverse('landing:schedule', args=(pk,)))
    else:
        checkBoxes = generateCheckBoxEntities(pk)
    return render(request, 'landing/selectcourses.html', {'checkBoxes': checkBoxes})

'''
@schedule send a request to render the schedule.html page
@param request: generates the response
@param pk: primary key corresponding to active user
'''
def schedule(request, pk):
    return render(request, 'landing/schedule.html')

'''
@createuser send a request to render the createuser.html page
@param request: generates the response
'''
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