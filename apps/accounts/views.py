from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .models import User

from django.contrib.auth.decorators import login_required


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("name")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

    return render(request, "accounts/login.html")


def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def dashboard_view(request):

    return render(request, "accounts/dashboard.html")


def user_list_view(request):

    users = User.objects.all()

    return render(
        request,
        "accounts/user_list.html",
        {
            "users": users
        }
    )