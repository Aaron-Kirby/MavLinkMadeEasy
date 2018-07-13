from django.db import models


# Models for static course backend data

class Course(models.Model):
    name = models.CharField(max_length=75)
    num = models.CharField(max_length=75)

    A ="All"
    S ="Spring"
    F ="Fall"
    M ="Summer"    
    SEM_CHOICE = (
        (A, "All"),
        (S, "Spring"),
        (F, "Fall"),
        (M, "Summer"),
        )
    semester = models.CharField(max_length=15,
                                choices=SEM_CHOICE,
                                default=A)          
    credits = models.IntegerField()
    prereqs = models.ManyToManyField('Prereq', related_name="needed", blank=True)

    N = "No"
    Y = "Lab"
    W = "Waiver"

    SPECIAL_TYPE_CHOICE = (
        (N, "No"),
        (Y, "Lab"),
        (W, "Waiver"),
        )
    special = models.CharField(max_length=15,
                           choices=SPECIAL_TYPE_CHOICE,
                           default=N)
    comment = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['num']

    def display_prereqs(self):
        return ', '.join([ prereq.num for prereq in self.prereqs.all() ])
    
    display_prereqs.short_description = 'Prereqs'

    def display_dept(self):
        return "%s" % (str.split(self.num)[0])

    def display_no(self):
        return "%s" % (str.split(self.num)[1])

    def __str__(self):
        return "%s | %s" % (self.num, self.name)

class Prereq(models.Model):
    prereq = models.ForeignKey('Course', on_delete=models.CASCADE)
    this_or = models.ForeignKey('Course', null=True, blank=True, related_name="synonymous", on_delete=models.CASCADE)

    C = "Corequisite"
    P = "Prerequisite"   
    REQ_CHOICE = (
            (C, "Corequisite"),
            (P, "Prerequisite"),
            )
    req_type = models.CharField(max_length=20,
                                choices=REQ_CHOICE,
                                null=True)
    class Meta:
        ordering = ['req_type']

    def display_recursive(self):
        return "%s -> " % (self.prereq.prereqs)

    def __str__(self):
        return "%s - %s / %s" % (self.req_type, self.prereq, self.this_or)

'''
Static degree type and associated requirements

'''

class Req(models.Model):
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    course = models.ManyToManyField(Course, related_name="required")

    GENE = 'General Education Requirements'
    DEPT = 'Department Requirements'
    ELEC = 'Electives'

    REQ_CHOICE = (
        (GENE, 'General Education Requirements'),
        (DEPT, 'Department Requirements'),
        (ELEC, 'Electives'),
        )
    
    req_type = models.CharField(max_length=50,
                                choices=REQ_CHOICE,
                                default=DEPT)
    def display_degrees(self):
        me = self.id
        return ', '.join([ degree.major for degree in Degree.objects.filter(req=me) ])

    def __str__(self):
        return "%s - %s" % (self.req_type, self.name)

class Degree(models.Model):    
    BS = 'Bachelor of Science'
    BA = 'Bachelor of Arts'
    GR = "Master's" 
    DEGREE_CHOICE = (
        (BS, 'Bachelor of Science'),
        (BA, 'Bachelor of Arts'),
        (GR, "Master's"),
        )
    degree = models.CharField(max_length=50,
                               choices=DEGREE_CHOICE,
                               default=BS)
    major = models.CharField(max_length=75)
    req = models.ManyToManyField(Req, blank=True, related_name="categories")
    
    def display_course_reqs(self):
        return ', '.join([ req.name for req in self.req.all() ])

    display_course_reqs.short_description = 'Requirements'

    def __str__(self):
        return "%s | %s" % (self.degree, self.major)

'''
Dynamic tables for users and associated courses needed/taken 

'''
class User(models.Model):
    email = models.CharField(max_length=75)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)

    class Meta:
        ordering = ['email']

    def display_degree(self):
        return "%s" % (self.degree)
    
    def __str__(self):
        return "%s" % (self.email)

class Complete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.ManyToManyField(Course, related_name="taken")
    
    def display_degree(self):
        return "%s\t%s" % (self.user.degree.major, self.user.degree.degree)

    def display_courses_completed(self):
        return ', '.join([ complete.name for complete in self.complete.all()])

    def display_credits_earned(self):
        x = 0
        for e in self.complete.all():
            x += e.credits
        return x

    display_credits_earned.short_description = 'Credits Earned'
    
    def display_credits_needed(self):
        y = 0
        for b in self.user.degree.req.all():
            y += b.credits
        return y

    display_credits_needed.short_description = 'Credits Needed (Total)'

    def display_courses_needed(self):
        return '\n'.join([ req.course.all() for req in self.user.degree.req.all()])

    display_courses_completed.short_description = 'Completed'
    
    def __str__(self):
        return "%s" % (self.user)

