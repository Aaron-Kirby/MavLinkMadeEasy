from django.contrib import admin
from .models import User
from .models import DegreePath
from .models import Courses
# Register your models here.

admin.site.register(User)
admin.site.register(DegreePath)
admin.site.register(Courses)
