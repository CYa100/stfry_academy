from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Academy Information",
            {
                "fields": (
                    "role",
                    "rank",
                    "status",
                    "telephone",
                    "dorm",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Academy Information",
            {
                "fields": (
                    "role",
                    "rank",
                    "status",
                    "telephone",
                    "dorm",
                )
            },
        ),
    )