from django.db import models
from django.conf import settings

from apps.academics.models import Classroom


class ClassroomEnrollment(models.Model):

    ROLE_CHOICES = (
        ("student", "Student"),
        ("teacher", "Teacher"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="classroom_enrollments"
    )

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} -> {self.classroom.name}"