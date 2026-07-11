import django_filters
from django import forms
from django.contrib.auth.models import User
from .models import Task


class TaskFilter(django_filters.FilterSet):
    """Фильтр для задач."""
    
    status = django_filters.ModelChoiceFilter(
        queryset=None,
        label='Статус',
        empty_label='---------'
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=None,
        label='Исполнитель',
        empty_label='---------'
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=None,
        label='Метка',
        empty_label='---------'
    )
    my_tasks = django_filters.BooleanFilter(
        label='Только свои задачи',
        method='filter_my_tasks',
        widget=forms.CheckboxInput
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'my_tasks']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Фильтруем queryset для полей
        self.filters['status'].queryset = Task._meta.get_field('status').related_model.objects.all()
        self.filters['executor'].queryset = User.objects.all()
        self.filters['labels'].queryset = Task._meta.get_field('labels').related_model.objects.all()
        
        # Если пользователь не указан, скрываем фильтр "Только мои задачи"
        if not user:
            self.filters.pop('my_tasks')

    def filter_my_tasks(self, queryset, name, value):
        """Фильтр задач по автору."""
        if value:
            user = self.request.user if hasattr(self, 'request') else None
            if user:
                return queryset.filter(author=user)
        return queryset
