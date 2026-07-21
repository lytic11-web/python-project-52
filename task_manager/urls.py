from django.contrib import admin
from django.urls import include, path

from users.views import UserLoginView, user_logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
    path("users/", include("users.urls")),
    path("statuses/", include("statuses.urls")),
    path("labels/", include("labels.urls")),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", user_logout, name="logout"),
]
