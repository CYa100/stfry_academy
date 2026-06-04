from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Dorm

from apps.accounts.models import User


def dorm_list(request):

    dorms = Dorm.objects.all()

    return render(
        request,
        "dorms/dorms.html",
        {
            "dorms": dorms
        }
    )


def dorm_detail(request, dorm_id):

    dorm = get_object_or_404(
        Dorm,
        id=dorm_id
    )

    users = User.objects.filter(
        dorm=dorm
    )

    return render(
        request,
        "dorms/dorm_detail.html",
        {
            "dorm": dorm,
            "users": users,
        }
    )