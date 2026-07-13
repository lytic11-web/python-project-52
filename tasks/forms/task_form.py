from django import forms
from django.contrib.auth.models import User
from tasks.models import Task


class TaskForm(forms.ModelForm):
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Исполнитель',
        required=False,
        empty_label='---------',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'labels': 'Метки',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }
