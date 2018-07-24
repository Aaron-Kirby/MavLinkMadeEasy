from django.test import TestCase

from ..views import *
from ..models import *

class YourTestClass(TestCase):

    def setUp(self):
        #Setup run before every test method.
        pass

    def tearDown(self):
        #Clean up run after every test method.
        # need to remove the user...
        pass

    def test_get_user_by_email(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="sample@test.com", degree=d)
        u.save()
        uID = u.id
        foundUser = getUserByEmail(u.email)
        self.assertTrue(u==foundUser)

    #def test_get_degree(self):
        #d = Degree(degree="Bachelor's of Science", major="CS")
        #d.save()
        #u = User(email="sample@test.com", degree=d)
        #u.save()
        #foundUser = getUserByEmail(u.email)
        #self.assertTrue(u==foundUser)