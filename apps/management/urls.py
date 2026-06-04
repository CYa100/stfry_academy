from django.urls import path

from .views import management_dashboard
from .views import management_base

from .views import faculty_management
from .views import lesson_management
from .views import class_management
from .views import dorm_management
from .views import user_management
from .views import enrollment_management

from .views import delete_faculty
from .views import delete_lesson
from .views import delete_classroom
from .views import delete_dorm
from .views import delete_user
from .views import delete_enrollment


urlpatterns = [

    path(
        "",
        management_dashboard,
        name="management_dashboard"
    ),

    path(
        "",
        management_base,
        name="management_base"
    ),

    # FACULTIES
    path(
        "faculties/",
        faculty_management,
        name="faculty_management"
    ),

    path(
        "faculties/delete/<int:id>/",
        delete_faculty,
        name="faculty_delete"
    ),

    # LESSONS
    path(
        "lessons/",
        lesson_management,
        name="lesson_management"
    ),

    path(
        "lessons/delete/<int:id>/",
        delete_lesson,
        name="delete_lesson"
    ),

    # CLASSES
    path(
        "classes/",
        class_management,
        name="class_management"
    ),

    path(
        "classes/delete/<int:id>/",
        delete_classroom,
        name="delete_classroom"
    ),

    # DORMS
    path(
        "dorms/",
        dorm_management,
        name="dorm_management"
    ),

    path(
        "dorms/delete/<int:id>/",
        delete_dorm,
        name="delete_dorm"
    ),

    # USERS
    path(
        "users/",
        user_management,
        name="user_management"
    ),

    path(
        "users/delete/<int:id>/",
        delete_user,
        name="delete_user"
    ),

    # ENROLLMENTS
    path(
        "enrollments/",
        enrollment_management,
        name="enrollment_management"
    ),

    path(
        "enrollments/delete/<int:id>/",
        delete_enrollment,
        name="delete_enrollment"
    ),

]