from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("admin", "Admin"),
    )

    STATUS_CHOICES = (
        ("freshman", "Freshman"),
        ("sophomore", "Sophomore"),
        ("junior", "Junior"),
        ("senior", "Senior"),
    )

    RANK_CHOICES = (
        ("S", "S"),
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("F", "F"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student"
    )

    rank = models.CharField(
        max_length=1,
        choices=RANK_CHOICES,
        default="F",
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="freshman"
    )

    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    dorm = models.ForeignKey(
        "dorms.Dorm",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"