from django.urls import path
from django.http import HttpResponse
from .views import IndexView


def users_list(request):
    return HttpResponse("Список пользователей (в разработке)")


def login_view(request):
    return HttpResponse("Вход (в разработке)")


def register_view(request):
    return HttpResponse("Регистрация (в разработке)")


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users/', users_list, name='users_list'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
