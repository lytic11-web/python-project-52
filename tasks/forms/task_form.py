from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    """Форма для создания и редактирования задачи."""

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
            # ПРИНУДИТЕЛЬНО делаем select multiple для меток!
            'labels': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }
