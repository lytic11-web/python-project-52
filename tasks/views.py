from django.http import HttpResponse


def index(request):
    """Главная страница с приветствием."""
    return HttpResponse('Welcome to Task Manager!')
