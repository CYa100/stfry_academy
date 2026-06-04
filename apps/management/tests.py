from django.test import TestCase, Client

from apps.academics.models import Faculty
from apps.academics.models import Lesson

from apps.dorms.models import Dorm

from apps.accounts.models import User

from apps.academics.models import Classroom

from django.urls import reverse

class FacultyTest(TestCase):

    def test_create_faculty(self):

        faculty = Faculty.objects.create(
            name="Engineering"
        )

        self.assertEqual(
            faculty.name,
            "Engineering"
        )


class DormTest(TestCase):

    def test_create_dorm(self):

        dorm = Dorm.objects.create(
            name="Dorm A",
            capacity=100
        )

        self.assertEqual(
            dorm.capacity,
            100
        )


class UserTest(TestCase):

    def test_create_user(self):

        user = User.objects.create_user(
            username="student1",
            password="123456"
        )

        self.assertEqual(
            user.username,
            "student1"
        )


class LessonTest(TestCase):

    def test_lesson_faculty_relation(self):

        faculty = Faculty.objects.create(
            name="Engineering"
        )

        lesson = Lesson.objects.create(
            name="Programming",
            faculty=faculty
        )

        self.assertEqual(
            lesson.faculty.name,
            "Engineering"
        )


class ClassroomTest(TestCase):

    def test_classroom_lesson_relation(self):

        faculty = Faculty.objects.create(
            name="Engineering"
        )

        lesson = Lesson.objects.create(
            name="Programming",
            faculty=faculty
        )

        classroom = Classroom.objects.create(
            name="A101",
            lesson=lesson
        )

        self.assertEqual(
            classroom.lesson.name,
            "Programming"
        )

        self.assertEqual(
            classroom.lesson.faculty.name,
            "Engineering"
        )


class LoginTest(TestCase):

    def setUp(self):

        User.objects.create_user(
            username="admin",
            password="123456"
        )

    def test_login(self):

        response = self.client.post(
            reverse("login"),
            {
                "name": "admin",
                "password": "123456"
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )


class FacultyIntegrationTest(TestCase):

    def setUp(self):

        self.client = Client()

        # admin user create
        self.user = User.objects.create_user(
            username="admin",
            password="123456"
        )

    def test_faculty_create_flow(self):

        # login
        login = self.client.login(
            username="admin",
            password="123456"
        )

        self.assertTrue(login)

        # faculty create request
        response = self.client.post(
            reverse("faculty_management"),
            {
                "name": "Engineering"
            }
        )

        # redirect / success control
        self.assertEqual(
            response.status_code,
            200
        )

        # DB control
        faculty_exists = Faculty.objects.filter(
            name="Engineering"
        ).exists()

        self.assertTrue(faculty_exists)