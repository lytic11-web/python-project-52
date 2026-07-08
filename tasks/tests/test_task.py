from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Status, Task


class TaskCRUDTest(TestCase):
    """Тесты CRUD для задач."""
    
    fixtures = ['statuses.json']

    def setUp(self):
        self.client = Client()
        # Создаём пользователя
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.user.set_password('testpass123')
        self.user.save()
        self.client.login(username='testuser', password='testpass123')
        
        # Создаём статус
        self.status = Status.objects.get(name='Новый')
        
        # Создаём задачу для тестов
        self.task = Task.objects.create(
            name='Тестовая задача',
            description='Описание',
            status=self.status,
            author=self.user
        )

    def test_task_list_requires_login(self):
        """Список задач требует авторизации."""
        self.client.logout()
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 302)

    def test_task_list_accessible(self):
        """Список задач доступен залогиненным."""
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая задача')

    def test_task_create(self):
        """Создание задачи."""
        response = self.client.post(reverse('task_create'), {
            'name': 'Новая задача',
            'description': 'Описание новой задачи',
            'status': self.status.pk,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='Новая задача').exists())
        
        # Проверяем, что автор установлен автоматически
        task = Task.objects.get(name='Новая задача')
        self.assertEqual(task.author, self.user)

    def test_task_update(self):
        """Обновление задачи."""
        response = self.client.post(
            reverse('task_update', args=[self.task.pk]),
            {
                'name': 'Обновлённая задача',
                'description': 'Новое описание',
                'status': self.status.pk,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Обновлённая задача')

    def test_task_delete_by_author(self):
        """Автор может удалить задачу."""
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(name='Тестовая задача').exists())

    def test_task_delete_by_non_author(self):
        """Не автор не может удалить задачу."""
        # Создаём другого пользователя
        other_user = User.objects.create_user(
            username='other',
            password='testpass123'
        )
        self.client.login(username='other', password='testpass123')
        
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)  # редирект
        self.assertTrue(Task.objects.filter(name='Тестовая задача').exists())  # задача не удалена

    def test_task_detail(self):
        """Просмотр задачи."""
        response = self.client.get(reverse('task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая задача')
