from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.academics.models import Faculty
from apps.academics.models import Lesson
from apps.academics.models import Classroom

from apps.dorms.models import Dorm

from apps.accounts.models import User

from apps.enrollments.models import ClassroomEnrollment

from django.contrib.auth.hashers import make_password


# --------------------------------------------------
# ADMIN CHECK
# --------------------------------------------------

def admin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        if request.user.role != "admin":
            return redirect("dashboard")

        return view_func(
            request,
            *args,
            **kwargs
        )

    return wrapper


# --------------------------------------------------
# MANAGEMENT DASHBOARD
# --------------------------------------------------

@admin_required
def management_dashboard(request):

    return render(
        request,
        "management/dashboard_management.html"
    )


# --------------------------------------------------
# MANAGEMENT BASE
# --------------------------------------------------

@admin_required
def management_base(request):

    return render(
        request,
        "management/base_management.html"
    )


# --------------------------------------------------
# FACULTY CRUD
# --------------------------------------------------

@csrf_exempt
def faculty_management(request):

    if request.method == "GET":

        faculties = Faculty.objects.all()

        return render(
            request,
            "management/faculties.html",
            {
                "faculties": faculties
            }
        )

    if request.method == "POST":

        faculty_id = request.POST.get("faculty_id")
        name = request.POST.get("name")

        # UPDATE
        if faculty_id:

            faculty = Faculty.objects.get(id=faculty_id)
            faculty.name = name
            faculty.save()

            return JsonResponse({
                "status": "updated",
                "id": faculty.id,
                "name": faculty.name
            })

        # CREATE
        else:

            faculty = Faculty.objects.create(name=name)

            return JsonResponse({
                "status": "created",
                "id": faculty.id,
                "name": faculty.name
            })
        
@csrf_exempt
def delete_faculty(request, id):

    if request.method == "POST":

        faculty = Faculty.objects.get(id=id)
        faculty.delete()

        return JsonResponse({
            "status": "deleted",
            "id": id
        })


# --------------------------------------------------
# LESSON CRUD
# --------------------------------------------------

@csrf_exempt
@admin_required
def lesson_management(request):

    if request.method == "GET":

        lessons = Lesson.objects.all()

        faculties = Faculty.objects.all()

        return render(
            request,
            "management/lessons.html",
            {
                "lessons": lessons,
                "faculties": faculties,
            }
        )

    if request.method == "POST":

        lesson_id = request.POST.get(
            "lesson_id"
        )

        name = request.POST.get(
            "name"
        )

        faculty_id = request.POST.get(
            "faculty"
        )

        faculty = Faculty.objects.get(
            id=faculty_id
        )

        # UPDATE
        if lesson_id:

            lesson = Lesson.objects.get(
                id=lesson_id
            )

            lesson.name = name

            lesson.faculty = faculty

            lesson.save()

            return JsonResponse({
                "status": "updated",
                "id": lesson.id,
                "name": lesson.name,
                "faculty_id": faculty.id,
                "faculty_name": faculty.name,
            })

        # CREATE
        else:

            lesson = Lesson.objects.create(
                name=name,
                faculty=faculty
            )

            return JsonResponse({
                "status": "created",
                "id": lesson.id,
                "name": lesson.name,
                "faculty_id": faculty.id,
                "faculty_name": faculty.name,
            })


@csrf_exempt
@admin_required
def delete_lesson(request, id):

    if request.method == "POST":

        lesson = get_object_or_404(
            Lesson,
            id=id
        )

        lesson.delete()

        return JsonResponse({
            "status": "deleted",
            "id": id
        })


# --------------------------------------------------
# CLASSROOM CRUD
# --------------------------------------------------

@csrf_exempt
@admin_required
def class_management(request):

    if request.method == "GET":

        classes = Classroom.objects.all()

        lessons = Lesson.objects.all()

        return render(
            request,
            "management/classes.html",
            {
                "classes": classes,
                "lessons": lessons,
            }
        )

    if request.method == "POST":

        classroom_id = request.POST.get(
            "classroom_id"
        )

        name = request.POST.get(
            "name"
        )

        lesson_id = request.POST.get(
            "lesson"
        )

        lesson = Lesson.objects.get(
            id=lesson_id
        )

        # UPDATE
        if classroom_id:

            classroom = Classroom.objects.get(
                id=classroom_id
            )

            classroom.name = name

            classroom.lesson = lesson

            classroom.save()

            return JsonResponse({
                "status": "updated",
                "id": classroom.id,
                "name": classroom.name,
                "lesson_id": lesson.id,
                "lesson_name": lesson.name,
            })

        # CREATE
        else:

            classroom = Classroom.objects.create(
                name=name,
                lesson=lesson
            )

            return JsonResponse({
                "status": "created",
                "id": classroom.id,
                "name": classroom.name,
                "lesson_id": lesson.id,
                "lesson_name": lesson.name,
            })


@csrf_exempt
@admin_required
def delete_classroom(request, id):

    if request.method == "POST":

        classroom = get_object_or_404(
            Classroom,
            id=id
        )

        classroom.delete()

        return JsonResponse({
            "status": "deleted",
            "id": id
        })


# --------------------------------------------------
# DORM CRUD
# --------------------------------------------------

@admin_required
def dorm_management(request):

    if request.method == "GET":

        dorms = Dorm.objects.all()

        return render(
            request,
            "management/dorms.html",
            {
                "dorms": dorms
            }
        )

    if request.method == "POST":

        dorm_id = request.POST.get("dorm_id")

        name = request.POST.get("name")

        capacity = request.POST.get("capacity")

        # UPDATE
        if dorm_id:

            dorm = get_object_or_404(
                Dorm,
                id=dorm_id
            )

            dorm.name = name
            dorm.capacity = capacity
            dorm.save()

            return JsonResponse({
                "status": "updated",
                "id": dorm.id,
                "name": dorm.name,
                "capacity": dorm.capacity
            })

        # CREATE
        else:

            dorm = Dorm.objects.create(
                name=name,
                capacity=capacity
            )

            return JsonResponse({
                "status": "created",
                "id": dorm.id,
                "name": dorm.name,
                "capacity": dorm.capacity
            })


@admin_required
def delete_dorm(request, id):

    if request.method == "POST":

        dorm = get_object_or_404(
            Dorm,
            id=id
        )

        dorm.delete()

        return JsonResponse({
            "status": "deleted",
            "id": id
        })


# --------------------------------------------------
# USER CRUD
# --------------------------------------------------

def user_management(request):

    if request.method == "GET":

        users = User.objects.all()
        dorms = Dorm.objects.all()

        return render(request, "management/users.html", {
            "users": users,
            "dorms": dorms
        })

    # CREATE / UPDATE
    if request.method == "POST":

        user_id = request.POST.get("user_id")

        username = request.POST.get("username")
        password = request.POST.get("password")

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        email = request.POST.get("email")
        telephone = request.POST.get("telephone")

        role = request.POST.get("role")
        rank = request.POST.get("rank")
        status = request.POST.get("status")

        dorm_id = request.POST.get("dorm")

        dorm = None
        if dorm_id:
            dorm = get_object_or_404(Dorm, id=dorm_id)

        # UPDATE
        if user_id:

            user = get_object_or_404(User, id=user_id)

            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.telephone = telephone
            user.role = role
            user.rank = rank
            user.status = status
            user.dorm = dorm

            user.save()

            return JsonResponse({
                "status": "updated",
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "telephone": user.telephone,
                "role": user.role,
                "rank": user.rank,
                "status_field": user.status,
                "dorm_id": user.dorm.id if user.dorm else "",
                "dorm_name": user.dorm.name if user.dorm else ""
            })

        # CREATE
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            role=role,
            rank=rank,
            status=status,
            dorm=dorm
        )

        return JsonResponse({
            "status": "created",
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "telephone": user.telephone,
            "role": user.role,
            "rank": user.rank,
            "status_field": user.status,
            "dorm_id": user.dorm.id if user.dorm else "",
            "dorm_name": user.dorm.name if user.dorm else ""
        })

def delete_user(request, id):

    if request.method == "POST":

        user = get_object_or_404(User, id=id)
        user.delete()

        return JsonResponse({
            "status": "deleted",
            "id": id
        })


# --------------------------------------------------
# ENROLLMENT CRUD
# --------------------------------------------------

@csrf_exempt
@admin_required
def enrollment_management(request):

    if request.method == "GET":

        enrollments = ClassroomEnrollment.objects.all()

        users = User.objects.all()

        classes = Classroom.objects.all()

        return render(
            request,
            "management/enrollments.html",
            {
                "enrollments": enrollments,
                "users": users,
                "classes": classes,
            }
        )

    if request.method == "POST":

        enrollment_id = request.POST.get("enrollment_id")

        user_id = request.POST.get("user")

        class_id = request.POST.get("classroom")

        role = request.POST.get("role")

        user = User.objects.get(id=user_id)

        classroom = Classroom.objects.get(id=class_id)

        # UPDATE
        if enrollment_id:

            enrollment = ClassroomEnrollment.objects.get(
                id=enrollment_id
            )

            enrollment.user = user

            enrollment.classroom = classroom

            enrollment.role = role

            enrollment.save()

            return JsonResponse({
                "status": "updated",
                "id": enrollment.id,
                "user_id": user.id,
                "username": user.username,
                "classroom_id": classroom.id,
                "classroom_name": f"{classroom.name} - {classroom.lesson.name}",
                "role": enrollment.role,
            })

        # CREATE
        else:

            enrollment = ClassroomEnrollment.objects.create(
                user=user,
                classroom=classroom,
                role=role
            )

            return JsonResponse({
                "status": "created",
                "id": enrollment.id,
                "user_id": user.id,
                "username": user.username,
                "classroom_id": classroom.id,
                "classroom_name": f"{classroom.name} - {classroom.lesson.name}",
                "role": enrollment.role,
            })


@csrf_exempt
@admin_required
def delete_enrollment(request, id):

    if request.method == "POST":

        enrollment = get_object_or_404(
            ClassroomEnrollment,
            id=id
        )

        enrollment.delete()

        return JsonResponse({
            "status": "deleted",
            "id": id
        })