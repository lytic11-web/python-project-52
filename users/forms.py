from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """Форма регистрации пользователя."""

    class Meta(UserCreationForm.Meta):
        model = User
        # Порядок полей как в демо
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        help_texts = {
            'username': 'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
            'password1': 'Ваш пароль должен содержать как минимум 3 символа.',
            'password2': 'Для подтверждения введите, пожалуйста, пароль ещё раз.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Убираем стандартные требования к паролю
        self.fields['password1'].help_text = 'Ваш пароль должен содержать как минимум 3 символа.'
        self.fields['password2'].help_text = 'Для подтверждения введите, пожалуйста, пароль ещё раз.'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'


class UserUpdateForm(forms.ModelForm):
    """Форма редактирования пользователя."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя',
        }
