from django.urls import path

from .views import dorm_list
from .views import dorm_detail

urlpatterns = [

    path("", dorm_list, name="dorms"),

    path(
        "<int:dorm_id>/",
        dorm_detail,
        name="dorm_detail"
    ),

]