from django.test import TestCase

from ..views import *
from ..models import *


class YourTestClass(TestCase):

    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(cself):
        # Clean up run after every test method.
        pass

    def test_get_user_by_email(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="sample@test.com", degree=d)
        u.save()
        foundUser = getUserByEmail(u.email)
        self.assertTrue(u == foundUser)

    def test_get_degree(self):
        deg = Degree(degree="Bachelor's of Science", major="CS")
        deg.save()
        foundDegree = getDegree("Bachelor's of Science", "CS")
        self.assertTrue(deg == foundDegree)

    def test_get_completed_by_user(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="completedbyuser@test.com", degree=d)
        u.save()
        uID = u.pk
        completed = Complete(user=u)
        completed.save()
        cc = Course(name="Java1", num="CIST1400", semester="A", credits=3, special="N")
        cc.save()
        completed.complete.add(cc)
        completed.save()
        self.assertTrue([cc] == getCompletedByUser(uID))

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

    def test_check_offered_semester(self):
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='Fall', credits=3)
        collegeAl.save()
        # print("CollegeAl semester is %s" % collegeAl.semester)
        currentMonth = datetime.now().month
        ssfSemester = getSemesterByMonthYear(currentMonth)
        # print("ssfSemester is %s" % ssfSemester)
        self.assertTrue(collegeAl.semester == ssfSemester)

    def test_get_semester_by_month_year(self):
        Spring = getSemesterByMonthYear(4)
        Summer = getSemesterByMonthYear(7)
        Fall = getSemesterByMonthYear(9)
        self.assertTrue(Spring == "Spring")
        self.assertTrue(Summer == "Summer")
        self.assertTrue(Fall == "Fall")

    def test_generate_new_semester(self):
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        testSemester = ["Spring", 2019, []]
        ssfSemester = getSemesterByMonthYear(currentMonth)
        semester = [ssfSemester, currentYear, []]
        currentSemester = generateNewSemester(semester)
        # print("current semester is %s" % currentSemester)
        self.assertTrue(currentSemester == testSemester)

    def test_is_full(self):
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        ssfSemester = getSemesterByMonthYear(currentMonth)
        semester = [ssfSemester, currentYear, []]
        currentSemester = generateNewSemester(semester)
        false = isFull(currentSemester[2])
        # still need to do the true case

    def test_email_found(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="email@test.com", degree=d)
        u.save()
        foundEmail = emailFound(u.email)
        self.assertTrue(foundEmail)

    def test_generate_major_dd(self):
        degreeOne = Degree(degree="Bachelor of Science", major="Computer Science")
        degreeOne.save()
        degrees = generateMajorDD()
        self.assertTrue([degreeOne.major] == degrees)

    def test_save_classes_to_user(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="sample@test.com", degree=d)
        u.save()
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='Fall', credits=3)
        collegeAl.save()
        classesChecked = [collegeAl.num]
        saveClassesToUser(classesChecked, u.pk)
        self.assertTrue(collegeAl.num == Complete.objects.get(user=u).complete.get(name="College Algebra").num)

    def test_remove_courses_taken(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="sample@test.com", degree=d)
        u.save()
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='Fall', credits=3)
        collegeAl.save()
        collegeAl2 = Course(id=2, name="College Algebra 2", num="MATH 1620", semester='Fall', credits=3)
        collegeAl2.save()
        classesReq = ["College Algebra", "College Algebra 2"]
        classesTaken = [collegeAl.name]
        result = removeCoursesTaken(classesReq, classesTaken)
        self.assertTrue(result == [collegeAl2.name])

    def test_remove_user_completed_entries(self):
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        u = User(email="sample@test.com", degree=d)
        u.save()
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='Fall', credits=3)
        collegeAl.save()
        collegeAl2 = Course(id=2, name="College Algebra 2", num="MATH 1620", semester='Fall', credits=3)
        collegeAl2.save()
        uID = u.pk
        completed = Complete(user=u)
        completed.save()
        completed.complete.add(collegeAl)
        completed.save()
        removeUserCompletedEnteries(uID)
        passed = False
        try:
            Complete.objects.get(user=u).complete.all()
        except:
            passed = True
        self.assertTrue(passed)

    def test_generate_checkbox_entities(self):
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='Fall', credits=3)
        collegeAl.save()
        reqs = Req(id=1, name="test", credits=3, req_type="Electives")
        reqs.save()
        reqs.course.add(collegeAl)
        reqs.save()
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        d.req.add(reqs)
        d.save()
        u = User(email="sample@test.com", degree=d)
        u.save()
        result = generateCheckBoxEntities(u.id)
        self.assertTrue(len(result) == 1)

    def test_get_courses_for_user(self):
        collegeAl = Course(id=1, name="College Algebra", num="MATH 1220", semester='Fall', credits=3)
        collegeAl.save()
        reqs = Req(id=1, name="test", credits=3, req_type="Electives")
        reqs.save()
        reqs.course.add(collegeAl)
        reqs.save()
        d = Degree(degree="Bachelor's of Science", major="CS")
        d.save()
        d.req.add(reqs)
        d.save()
        u = User(email="sample@test.com", degree=d)
        u.save()
        courses = getCoursesForUser(u.id)
        self.assertTrue(courses[0].name == collegeAl.name)