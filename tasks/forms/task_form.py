from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    """Форма для создания и редактирования задачи."""

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'labels': forms.CheckboxSelectMultiple(),
        }
