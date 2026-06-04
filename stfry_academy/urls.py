from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("academics/", include("apps.academics.urls")),
    path("dorms/", include("apps.dorms.urls")),
    path("management/", include("apps.management.urls")),
]