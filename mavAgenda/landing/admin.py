from django.contrib import admin
from .models import User, DegreePath, Course
# Register your models here.

admin.site.register(User)
admin.site.register(DegreePath)
admin.site.register(Course)

