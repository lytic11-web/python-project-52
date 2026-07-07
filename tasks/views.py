from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from .models import Status


class IndexView(TemplateView):
    """Главная страница."""
    template_name = 'tasks/index.html'


class StatusListView(LoginRequiredMixin, ListView):
    """Список всех статусов."""
    model = Status
    template_name = 'tasks/status_list.html'
    context_object_name = 'statuses'
    ordering = ['-created_at']


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Создание нового статуса."""
    model = Status
    fields = ['name']
    template_name = 'tasks/status_create.html'
    success_url = reverse_lazy('status_list')
    success_message = 'Статус успешно создан'


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Редактирование статуса."""
    model = Status
    fields = ['name']
    template_name = 'tasks/status_update.html'
    success_url = reverse_lazy('status_list')
    success_message = 'Статус успешно изменен'


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление статуса."""
    model = Status
    template_name = 'tasks/status_delete.html'
    success_url = reverse_lazy('status_list')

    def post(self, request, *args, **kwargs):
        """Переопределяем post для обработки ProtectedError."""
        try:
            messages.success(request, 'Статус успешно удален')
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, 'Невозможно удалить статус')
            return redirect('status_delete', pk=self.get_object().pk)
