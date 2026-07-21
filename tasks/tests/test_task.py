from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from statuses.models import Status
from tasks.models import Task


class TaskCRUDTest(TestCase):
    """Тесты CRUD для задач."""

    fixtures = ["statuses.json"]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")
        self.status = Status.objects.get(name="Новый")

    def test_task_list(self):
        """Список задач."""
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        """Создание задачи."""
        response = self.client.post(
            reverse("task_create"),
            {
                "name": "Тестовая задача",
                "status": self.status.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Task.objects.filter(name="Тестовая задача").exists()
        )

    def test_task_update(self):
        """Обновление задачи."""
        task = Task.objects.create(
            name="Старая задача", status=self.status, author=self.user
        )
        response = self.client.post(
            reverse("task_update", args=[task.pk]),
            {
                "name": "Новая задача",
                "status": self.status.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.name, "Новая задача")

    def test_task_delete(self):
        """Удаление задачи."""
        task = Task.objects.create(
            name="Удаляемая задача", status=self.status, author=self.user
        )
        response = self.client.post(
            reverse("task_delete", args=[task.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Task.objects.filter(name="Удаляемая задача").exists()
        )
