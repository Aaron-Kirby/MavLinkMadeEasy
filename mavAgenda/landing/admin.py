from django.contrib import admin
from .models import User
from .models import UserCompleted
from .models import PossibleDegrees
from .models import RequirementCategories
from .models import Course
from .models import CoursePrereqs
from .models import CoreCourse
from .models import EnglishCourse
from .models import MathCourse
from .models import SpeechCourse
# Register your models here.

admin.site.register(User)
admin.site.register(UserCompleted)
admin.site.register(PossibleDegrees)
admin.site.register(RequirementCategories)
admin.site.register(Course)
admin.site.register(CoursePrereqs)
admin.site.register(CoreCourse)
admin.site.register(EnglishCourse)
admin.site.register(MathCourse)
admin.site.register(SpeechCourse)
