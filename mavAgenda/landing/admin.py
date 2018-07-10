from django.contrib import admin
from .models import Course, Degree, ReqType, Prereq
from .models import User, UserCompleted

# Register models below

admin.site.register(User)
admin.site.register(UserCompleted)
admin.site.register(Course)
# admin.site.register(Degree)
admin.site.register(Prereq)
admin.site.register(ReqType)

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('degree', 'major', 'concentration')
    list_filter = ('level', 'major')
    fields = ['degree', ('major', 'concentration')]

admin.site.register(Degree, DegreeAdmin)
