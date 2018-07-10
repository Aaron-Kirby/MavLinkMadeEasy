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

    def __str__(self):
        return str(self.name)

class Prereq(models.Model):
    prereq = models.ForeignKey('Course', on_delete=models.CASCADE)
    C = "Corequisite"
    P = "Prerequisite"   
    
    this_or = models.ForeignKey('Course', null=True, blank=True, related_name="synonymous", on_delete=models.CASCADE)

    REQ_CHOICE = (
            (C, "Corequisite"),
            (P, "Prerequisite"),
            )
    req_type = models.CharField(max_length=20,
                                choices=REQ_CHOICE,
                                null=True)
    class Meta:
        ordering = ['req_type']

    def __str__(self):
        return str(self.prereq)

'''
Static degree type and associated requirements

'''

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
    reqtypes = models.ManyToManyField(ReqType)

#    def display_concentration(self):
#        return ', '.join([ concentration.name for concentration in self.concentration.all()])
    
#    display_concentration.short_description = 'Concentration'
    
    def __str__(self):
        return "%s | %s" % (self.degree, self.major)

#class Concentration(models.Model):
#    degree = models.ForeignKey(Degree, on_delete=models.CASCADE) 
#    name = models.CharField(max_length=100)
#    credits = models.IntegerField()
#    reqs = models.ForeignKey(ReqType, on_delete=models.PROTECT)

class ReqType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Requirement Fulfilled")
    credits = models.IntegerField()
    course = models.ManyToManyField(Course)
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
    def __str__(self):
        return "%s - %s" % (self.req_type, self.name)


'''
Dynamic tables for users and associated courses needed/taken 

'''
class User(models.Model):
    email = models.CharField(max_length=75, editable=False)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)

    class Meta:
        ordering = ['degree']
    
    def __str__(self):
        return "%s | %s" % (self.degree, self.email)

class UserCompleted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursenumber = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.coursenumber





'''
class ReqCategories(models.Model):    
    core = models.ForeignKey(Core, on_delete=models.PROTECT)
    core_credits = models.IntegerField()
    # 'fundamental academjc skills
    eng = models.ForeignKey(English, on_delet=models.()
    eng_credits = models.IntegerField(default=9)
    math = models.IntegerField()
    math_credits = models.IntegerField(default=3)
    speech = models.IntegerField()
    speech_credits = models.IntegerField()

    def __str__(self):
        return self.core

        '''
