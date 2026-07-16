from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from tasks.models import Label


class LabelListView(LoginRequiredMixin, ListView):
    """Список всех меток."""

    model = Label
    template_name = "tasks/label_list.html"
    context_object_name = "labels"
    ordering = ["-created_at"]


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Создание новой метки."""

    model = Label
    fields = ["name"]
    template_name = "tasks/label_create.html"
    success_url = reverse_lazy("label_list")
    success_message = "Метка успешно создана"


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Редактирование метки."""

    model = Label
    fields = ["name"]
    template_name = "tasks/label_update.html"
    success_url = reverse_lazy("label_list")
    success_message = "Метка успешно изменена"


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление метки."""

    model = Label
    template_name = "tasks/label_delete.html"
    success_url = reverse_lazy("label_list")

    def post(self, request, *args, **kwargs):
        """Проверяем, связана ли метка с задачами."""
        label = self.get_object()
        if label.tasks.exists():
            messages.error(
                request, "Невозможно удалить метку, потому что она используется"
            )
            return redirect("label_delete", pk=label.pk)

        messages.success(request, "Метка успешно удалена")
        return super().post(request, *args, **kwargs)
