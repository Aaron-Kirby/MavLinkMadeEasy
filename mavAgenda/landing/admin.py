from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Course, Degree, Req, Prereq, User, Complete

# Register models below

# admin.site.register(User)
# admin.site.register(Complete)
# admin.site.register(Course)
# admin.site.register(Degree)
# admin.site.register(Prereq)
# admin.site.register(Req)

admin.site.site_header = 'Mavlink - Made Easy'
admin.site.site_title = "pyParty Admin"

class ReqAdmin(admin.ModelAdmin):
    list_display = ('name', 'credits', 'req_type', 'display_degrees')
    list_filter = ('req_type', 'name')

admin.site.register(Req, ReqAdmin)

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('degree', 'major')
    list_filter = ('degree', 'req')
    filter_horizontal = ['req']
    fields = [('degree', 'major'), 'req']

admin.site.register(Degree, DegreeAdmin)

class PrereqAdmin(admin.ModelAdmin):
    list_display = ('prereq', 'this_or','req_type')
    list_filter = ('prereq', 'this_or')
    fields = ['req_type', ('prereq', 'this_or')]

#class PrereqInline(admin.TabularInline):s

admin.site.register(Prereq, PrereqAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('num', 'name', 'special', 'credits')
    list_filter = ('semester', 'special')
    filter_horizontal = ['prereqs']
    fields = [('name', 'num'), 'credits', 'semester', 'prereqs', ('special', 'comment')]
    search_fields=['num', 'name']
#    inlines = [PrereqInline]


admin.site.register(Course, CourseAdmin)

class CompleteAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_courses_completed', 'display_degree', 'display_credits_earned', 'display_credits_needed')
    filter_horizontal = ['complete']   
#list_filter = ['display_degree'] 

#class CompleteInline(admin.TabularInline):
#    model = Complete

admin.site.register(Complete, CompleteAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'degree')
    list_filter = ['degree']

#    inlines = [CompleteInline]

admin.site.register(User, UserAdmin)
