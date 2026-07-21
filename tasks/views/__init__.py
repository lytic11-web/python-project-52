from django.views.generic import TemplateView

from .task_views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
)


class IndexView(TemplateView):
    """Главная страница."""
    template_name = "tasks/index.html"


__all__ = [
    "IndexView",
    "TaskListView",
    "TaskCreateView",
    "TaskUpdateView",
    "TaskDeleteView",
    "TaskDetailView",
]
