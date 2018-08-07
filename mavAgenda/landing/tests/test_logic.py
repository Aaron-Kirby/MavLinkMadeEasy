from django.test import TestCase

from ..views import *
from ..models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class YourTestClass(TestCase):

    def setUp(self):
        #Setup run before every test method.
        pass

    def tearDown(cself):
        #Clean up run after every test method.
        pass

    def test_get_user_by_email(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="sample@test.com", degree=d)
        u.save()
        foundUser = getUserByEmail(u.email)
        self.assertTrue(u==foundUser)

    def test_get_degree(self):
        deg = Degree(degree="Bachelor's of Science", major="CS")
        deg.save()
        foundDegree = getDegree("Bachelor's of Science", "CS")
        self.assertTrue(deg==foundDegree)

    def test_get_completed_by_user(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="completedbyuser@test.com", degree=d)
        u.save()
        uID = u.pk
        completed = Complete(user=u)
        completed.save()
        cc = Course(name="Java1", num="CIST1400", semester = "A", credits=3, special="N")
        cc.save()
        completed.complete.add(cc)
        completed.save()
        self.assertTrue([cc] == getCompletedByUser(uID))

    #def test_check_course_valid(self):
        #d = Degree(degree="Bachelor's of Science", major="CS")
        #d.save()
        #u = User(email="completedbyuser@test.com", degree=d)
        #u.save()
        #uID = u.pk
        #completed = Complete(user=u)
        #completed.save()
        #cc = Course(name="Java1", num="CIST1400", semester="A", credits=3, special="N")
        #cc.save()
        #completed.complete.add(cc)
        #completed.save()
        #print("completed: %s" % Complete.objects.get(user=u).complete.all())


    #def test_get_courses_for_user(self):

    #def test_remove_courses_taken(self):

    def test_check_prereqs_met(self):
        classesTaken = []
        prereqs = []
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='All', credits=3)
        collegeAl.save()
        coAl = Prereq(id=3, prereq=collegeAl, req_type="Prerequisite")
        coAl.save()
        precalcAlgebra = Course(id=2, name="Pre-Calculus Algebra", num="MATH 1320", semester='All', credits=3)
        precalcAlgebra.save()
        precalcAlgebra.prereqs.add(coAl)
        precalcAlgebra.save()
        pr = Course.objects.get(name="Pre-Calculus Algebra").prereqs.all()
        for p in pr:
            prereqs.append(p)
        c1 = Course.objects.get(name="College Algebra")
        classesTaken.append(c1)
        self.assertTrue(checkPrereqsMet(pr, classesTaken, []))

    def test_check_prereqs_met_with_thisor(self):
        classesTaken = []
        prereqs = []
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='All', credits=3)
        collegeAl.save()
        test = Course(id=2, name="Testing", num="TEST 1234", semester='All', credits=3)
        test.save()
        pr = Prereq(id=3, prereq=collegeAl, this_or=test, req_type="Prerequisite")
        pr.save()
        precalcAlgebra = Course(id=2, name="Pre-Calculus Algebra", num="MATH 1320", semester='All', credits=3)
        precalcAlgebra.save()
        precalcAlgebra.prereqs.add(pr)
        precalcAlgebra.save()
        pr = Course.objects.get(name="Pre-Calculus Algebra").prereqs.all()
        for p in pr:
            prereqs.append(p)
        classesTaken.append(test)
        self.assertTrue(checkPrereqsMet(pr, classesTaken, []))

    #def test_check_offered_semester(self):

    #def test_check_course_valid(self):

    #def test_get_semester_by_month_year(self):

    #def test_generate_new_semester(self):

    #def test_is_full(self):

    #def test_create_schedule(self):

    #def test_generate_checkbox_entities(self):

    #def test_generate_major_id(self):

    def test_email_found(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="email@test.com", degree=d)
        u.save()
        foundEmail = emailFound(u.email)
        self.assertTrue(foundEmail)

    #def test_save_classes_to_user(self):

    #def test_remove_user_completed_entries(self):