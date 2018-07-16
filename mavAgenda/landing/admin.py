from django.contrib import admin
from .models import Course, Degree, Req, Prereq, User, Complete

# Register models below

admin.site.register(User)
admin.site.register(Complete)
admin.site.register(Course)
# admin.site.register(Degree)
admin.site.register(Prereq)
admin.site.register(Req)


class DegreeAdmin(admin.ModelAdmin):
    list_display = ('degree', 'major')
    list_filter = ('degree', 'major')
    fields = ['degree', 'major', 'req']

admin.site.register(Degree, DegreeAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('num', 'name', 'special', 'credits')
    list_filter = ('semester', 'special')
    search_fields=['prereq__prereq', 'prereq__this_or']
