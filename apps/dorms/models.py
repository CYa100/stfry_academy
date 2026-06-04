from django.db import models


class Dorm(models.Model):

    name = models.CharField(max_length=100)

    capacity = models.IntegerField(default=800)

    def __str__(self):
        return self.name