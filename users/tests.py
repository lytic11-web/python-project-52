from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserRegistrationTest(TestCase):
    """C — Create (регистрация)."""
    
    def test_registration_creates_user(self):
        """Регистрация создаёт пользователя."""
        data = {
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'username': 'ivan',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # редирект
        self.assertTrue(User.objects.filter(username='ivan').exists())


class UserUpdateTest(TestCase):
    """U — Update (обновление)."""
    
    fixtures = ['users.json']

    def setUp(self):
        self.user = User.objects.get(username='testuser')
        self.user.set_password('testpass123')
        self.user.save()
        self.client.login(username='testuser', password='testpass123')

    def test_user_can_update_profile(self):
        """Пользователь может обновить свой профиль."""
        response = self.client.post(
            reverse('user_update', args=[self.user.pk]),
            {'first_name': 'Пётр', 'last_name': 'Петров', 'username': 'testuser'}
        )
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Пётр')


class UserDeleteTest(TestCase):
    """D — Delete (удаление)."""
    
    fixtures = ['users.json']

    def setUp(self):
        self.user = User.objects.get(username='testuser')
        self.user.set_password('testpass123')
        self.user.save()
        self.client.login(username='testuser', password='testpass123')

    def test_user_can_delete_account(self):
        """Пользователь может удалить свой аккаунт."""
        response = self.client.post(reverse('user_delete', args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())
