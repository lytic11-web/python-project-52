from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="users_list"),
    path("create/", views.UserRegistrationView.as_view(), name="register"),
    path(
        "<int:pk>/update/", views.UserUpdateView.as_view(), name="user_update"
    ),
    path(
        "<int:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete"
    ),
    path("login/", views.UserLoginView.as_view(), name="login"),
]
