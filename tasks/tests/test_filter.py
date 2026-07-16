from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from tasks.models import Label, Status, Task


class TaskFilterTest(TestCase):
    """Тесты фильтрации задач."""

    fixtures = ["statuses.json"]

    def setUp(self):
        self.client = Client()

        # Создаём пользователей
        self.user1 = User.objects.create_user(
            username="user1", password="testpass123"
        )
        self.user2 = User.objects.create_user(
            username="user2", password="testpass123"
        )

        # Создаём статусы
        self.status_new = Status.objects.get(name="Новый")
        self.status_work = Status.objects.get(name="В работе")

        # Создаём метку
        self.label = Label.objects.create(name="Тестовая")

        # Создаём задачи
        self.task1 = Task.objects.create(
            name="Задача 1",
            status=self.status_new,
            author=self.user1,
            executor=self.user2,
        )
        self.task1.labels.add(self.label)

        self.task2 = Task.objects.create(
            name="Задача 2",
            status=self.status_work,
            author=self.user2,
            executor=self.user1,
        )

        self.client.login(username="user1", password="testpass123")

    def test_filter_by_status(self):
        """Фильтрация по статусу."""
        response = self.client.get(
            reverse("task_list"), {"status": self.status_new.pk}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Задача 1")
        self.assertNotContains(response, "Задача 2")

    def test_filter_by_executor(self):
        """Фильтрация по исполнителю."""
        response = self.client.get(
            reverse("task_list"), {"executor": self.user1.pk}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Задача 2")
        self.assertNotContains(response, "Задача 1")

    def test_filter_by_label(self):
        """Фильтрация по метке."""
        response = self.client.get(
            reverse("task_list"), {"labels": self.label.pk}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Задача 1")
        self.assertNotContains(response, "Задача 2")

    def test_filter_my_tasks(self):
        """Фильтр 'Только свои задачи'."""
        response = self.client.get(reverse("task_list"), {"my_tasks": "on"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Задача 1")
        self.assertNotContains(response, "Задача 2")

    def test_combined_filter(self):
        """Комбинированная фильтрация."""
        response = self.client.get(
            reverse("task_list"),
            {"status": self.status_new.pk, "my_tasks": "on"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Задача 1")
        self.assertNotContains(response, "Задача 2")
