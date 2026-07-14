from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.shortcuts import redirect
from tasks.models import Task
from tasks.forms import TaskForm
from django_filters.views import FilterView
from tasks.filters import TaskFilter


class TaskListView(LoginRequiredMixin, FilterView):
    """Список всех задач с фильтрацией."""
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    ordering = ['-created_at']

    def get_filterset_kwargs(self, filterset_class):
        """Передаём текущего пользователя в фильтр."""
        kwargs = super().get_filterset_kwargs(filterset_class)
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        """Получаем queryset с применёнными фильтрами."""
        queryset = super().get_queryset()
        
        # Если выбран фильтр "Только мои задачи"
        if self.request.GET.get('my_tasks'):
            queryset = queryset.filter(author=self.request.user)
        
        return queryset


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


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """Удаление задачи."""
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')
    success_message = 'Задача успешно удалена'

    def test_func(self):
        """Только автор может удалить задачу."""
        return self.request.user.pk == self.get_object().pk

    def handle_no_permission(self):
        """Если не автор — редирект с сообщением."""
        messages.error(self.request, 'Задачу может удалить только ее автор')
        return redirect('task_list')


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Просмотр задачи."""
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
