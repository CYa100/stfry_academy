from django.db import models


class Faculty(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name


class Lesson(models.Model):

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name="lessons"
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Classroom(models.Model):

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="classes"
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name