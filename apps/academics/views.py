from django.shortcuts import render

from .models import Faculty
from .models import Lesson
from .models import Classroom

from django.shortcuts import get_object_or_404

from apps.enrollments.models import ClassroomEnrollment


def faculty_list(request):

    faculties = Faculty.objects.all()

    return render(request, "academics/faculties.html", {
        "faculties": faculties
    })


def lesson_list(request):

    lessons = Lesson.objects.all()

    return render(request, "academics/lessons.html", {
        "lessons": lessons
    })


def classroom_list(request):

    classes = Classroom.objects.all()

    return render(request, "academics/classes.html", {
        "classes": classes
    })

def classroom_detail(request, class_id):

    classroom = get_object_or_404(
        Classroom,
        id=class_id
    )

    enrollments = classroom.enrollments.all()

    return render(
        request,
        "academics/classroom_detail.html",
        {
            "classroom": classroom,
            "enrollments": enrollments,
        }
    )