from django.test import TestCase

from ..views import *
from ..models import *

class YourTestClass(TestCase):

    def setUp(self):
        #Setup run before every test method.
        pass

    def tearDown(self):
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

    def test_check_prereqs(self):
        classesTaken = []
        prereqs = []
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='All', credits=3 )
        collegeAl.save()
        coAl = Prereq(id=3, prereq=collegeAl, req_type="Prerequisite")
        coAl.save()
        precalcAlgebra=Course(id=2, name="Pre-Calculus Algebra", num="MATH 1320", semester='All', credits=3)
        precalcAlgebra.save()
        precalcAlgebra.prereqs.add(coAl)
        precalcAlgebra.save()
        pr = Course.objects.get(name="Pre-Calculus Algebra").prereqs.all()
        for p in pr:
            prereqs.append(p)
        c1 = Course.objects.get(name="College Algebra")
        classesTaken.append(c1)
        self.assertTrue(checkPrereqsMet(pr, classesTaken))

    def test_check_prereqs_with_thisor(self):
        classesTaken = []
        prereqs = []
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='All', credits=3 )
        collegeAl.save()
        test = Course(id=2, name="Testing", num="TEST 1234", semester='All', credits=3)
        test.save()
        pr = Prereq(id=3, prereq=collegeAl, this_or=test, req_type="Prerequisite")
        pr.save()
        precalcAlgebra=Course(id=2, name="Pre-Calculus Algebra", num="MATH 1320", semester='All', credits=3)
        precalcAlgebra.save()
        precalcAlgebra.prereqs.add(pr)
        precalcAlgebra.save()
        pr = Course.objects.get(name="Pre-Calculus Algebra").prereqs.all()
        for p in pr:
            prereqs.append(p)
        print( "Prereqs (Options): %s" % prereqs)
        #t = Course.objects.get(name="Testing")
        classesTaken.append(test)
        print( "Classes taken: %s" % classesTaken )
        self.assertTrue(checkPrereqsMet(pr, classesTaken))