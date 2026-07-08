from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Status


class StatusCRUDTest(TestCase):
    """Тесты CRUD для статусов."""
    
    fixtures = ['statuses.json']

    def setUp(self):
        self.client = Client()
        # Создаём пользователя для тестов
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_status_list_requires_login(self):
        """Список статусов требует авторизации."""
        self.client.logout()
        response = self.client.get(reverse('status_list'))
        self.assertEqual(response.status_code, 302)  # редирект на login

    def test_status_list_accessible(self):
        """Список статусов доступен залогиненным."""
        response = self.client.get(reverse('status_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Новый')

    def test_status_create(self):
        """Создание статуса."""
        response = self.client.post(reverse('status_create'), {'name': 'Завершён'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='Завершён').exists())

    def test_status_update(self):
        """Обновление статуса."""
        status = Status.objects.get(name='Новый')
        response = self.client.post(
            reverse('status_update', args=[status.pk]),
            {'name': 'Обновлённый'}
        )
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, 'Обновлённый')

    def test_status_delete(self):
        """Удаление статуса."""
        status = Status.objects.get(name='Новый')
        response = self.client.post(reverse('status_delete', args=[status.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(name='Новый').exists())
