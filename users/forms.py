from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """Форма регистрации пользователя."""

    first_name = forms.CharField(
        label='Имя',
        max_length=30,
        required=True,
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=30,
        required=True,
    )
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        required=True,
        help_text='Ваш пароль должен содержать как минимум 8 символов.'
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        required=True,
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.'
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    """Форма редактирования пользователя."""

    first_name = forms.CharField(label='Имя', max_length=30, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=30, required=True)
    username = forms.CharField(label='Имя пользователя', max_length=150, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
