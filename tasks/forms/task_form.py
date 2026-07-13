from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executor': 'Исполнитель',
            'labels': 'Метки',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            # Явно указываем виджет Select
            'executor': forms.Select(attrs={'class': 'form-select'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }
