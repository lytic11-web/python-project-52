from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import UserRegistrationForm, UserUpdateForm, UserLoginForm


class UserListView(ListView):
    """Список всех пользователей."""
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserRegistrationView(SuccessMessageMixin, CreateView):
    """Регистрация нового пользователя."""
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """Редактирование пользователя."""
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_list')
    success_message = 'Пользователь успешно изменен'

    def test_func(self):
        """Только сам пользователь может редактировать свой профиль."""
        return self.request.user.pk == self.get_object().pk

    def form_valid(self, form):
        # Если введены пароли и они совпадают, обновляем пароль пользователя
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1 and password2 and password1 == password2:
            self.object = form.save(commit=False)
            self.object.set_password(password1)
            self.object.save()
            return super().form_valid(form)
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление пользователя."""
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('index')
    success_message = 'Пользователь успешно удален'

    def test_func(self):
        """Только сам пользователь может удалить свой профиль."""
        return self.request.user.pk == self.get_object().pk


class UserLoginView(SuccessMessageMixin, LoginView):
    """Вход в систему."""
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_message = 'Вы залогинены'

    def get_success_url(self):
        return reverse_lazy('index')


def user_logout(request):
    """Выход из системы."""
    logout(request)
    messages.success(request, 'Вы разлогинены')
    return redirect('index')
