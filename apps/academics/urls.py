from django.urls import path

from .views import faculty_list
from .views import lesson_list
from .views import classroom_list

from .views import classroom_detail

urlpatterns = [

    path("faculties/", faculty_list, name="faculties"),

    path("lessons/", lesson_list, name="lessons"),

    path("classes/", classroom_list, name="classes"),

    path("classes/<int:class_id>/", classroom_detail, name="classroom_detail"),
]