from django.contrib import admin

from .models import Faculty
from .models import Lesson
from .models import Classroom


admin.site.register(Faculty)
admin.site.register(Lesson)
admin.site.register(Classroom)