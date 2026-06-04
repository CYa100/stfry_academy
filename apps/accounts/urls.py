from django.urls import path
from .views import login_view
from .views import logout_view
from .views import dashboard_view
from .views import user_list_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("users/", user_list_view, name="user_list"),
]