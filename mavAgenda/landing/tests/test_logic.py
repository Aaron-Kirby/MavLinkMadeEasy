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

    #for user at inception
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
        print(cc)
        completed.complete.add(cc)
        completed.save()
        print(getCompletedByUser(uID))
        self.assertTrue([cc] == getCompletedByUser(uID))


    def test_get_courses_for_user(self):

    #def test_remove_courses_taken(self):

    #def test_check_prereq_met(self):

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
