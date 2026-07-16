from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from tasks.models import Status


class IndexView(TemplateView):
    """Главная страница."""

    template_name = "tasks/index.html"


class StatusListView(LoginRequiredMixin, ListView):
    """Список всех статусов."""

    model = Status
    template_name = "tasks/status_list.html"
    context_object_name = "statuses"
    ordering = ["-created_at"]


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Создание нового статуса."""

    model = Status
    fields = ["name"]
    template_name = "tasks/status_create.html"
    success_url = reverse_lazy("status_list")
    success_message = "Статус успешно создан"


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Редактирование статуса."""

    model = Status
    fields = ["name"]
    template_name = "tasks/status_update.html"
    success_url = reverse_lazy("status_list")
    success_message = "Статус успешно изменен"


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление статуса."""

    model = Status
    template_name = "tasks/status_delete.html"
    success_url = reverse_lazy("status_list")

    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if status.task_set.exists():
            messages.error(request, "Невозможно удалить статус")
            return redirect("status_delete", pk=status.pk)

        messages.success(request, "Статус успешно удален")
        return super().post(request, *args, **kwargs)
