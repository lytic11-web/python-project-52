from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from labels.models import Label
from statuses.models import Status
from tasks.models import Task


class TaskFilterTest(TestCase):
    """Тесты фильтрации задач."""

    fixtures = ["statuses.json"]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")
        self.status = Status.objects.get(name="Новый")

    def test_filter_by_status(self):
        """Фильтр по статусу."""
        Task.objects.create(
            name="Задача 1", status=self.status, author=self.user
        )
        response = self.client.get(
            reverse("task_list"), {"status": self.status.pk}
        )
        self.assertEqual(response.status_code, 200)

    def test_filter_by_label(self):
        """Фильтр по метке."""
        label = Label.objects.create(name="Важно")
        task = Task.objects.create(
            name="Задача с меткой", status=self.status, author=self.user
        )
        task.labels.add(label)
        response = self.client.get(
            reverse("task_list"), {"labels": label.pk}
        )
        self.assertEqual(response.status_code, 200)
