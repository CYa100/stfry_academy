from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "member_id",
            "name",
            "surname",
            "role",
            "rank",
            "status",
            "dorm_id",
            "email",
            "password",
            "telephone",
        )