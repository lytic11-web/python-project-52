from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.shortcuts import redirect
from tasks.models import Task
from tasks.forms import TaskForm


class TaskListView(LoginRequiredMixin, ListView):
    """Список всех задач."""
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Создание новой задачи."""
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')
    success_message = 'Задача успешно создана'

    def form_valid(self, form):
        """Автоматически устанавливаем автора задачи."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Редактирование задачи."""
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('task_list')
    success_message = 'Задача успешно изменена'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление задачи."""
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')

    def post(self, request, *args, **kwargs):
        """Проверяем, что задачу удаляет только её автор."""
        task = self.get_object()
        if task.author != request.user:
            messages.error(request, 'Задачу может удалить только ее автор')
            return redirect('task_detail', pk=task.pk)
        
        messages.success(request, 'Задача успешно удалена')
        return super().post(request, *args, **kwargs)


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Просмотр задачи."""
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
