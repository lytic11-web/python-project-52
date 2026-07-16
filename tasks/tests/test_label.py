from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from tasks.models import Label, Status, Task


class LabelCRUDTest(TestCase):
    """Тесты CRUD для меток."""

    fixtures = ["statuses.json"]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.user.set_password("testpass123")
        self.user.save()
        self.client.login(username="testuser", password="testpass123")

        self.status = Status.objects.get(name="Новый")

        self.label = Label.objects.create(name="Тестовая метка")

    def test_label_list_requires_login(self):
        """Список меток требует авторизации."""
        self.client.logout()
        response = self.client.get(reverse("label_list"))
        self.assertEqual(response.status_code, 302)

    def test_label_list_accessible(self):
        """Список меток доступен залогиненным."""
        response = self.client.get(reverse("label_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовая метка")

    def test_label_create(self):
        """Создание метки."""
        response = self.client.post(
            reverse("label_create"), {"name": "Новая метка"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name="Новая метка").exists())

    def test_label_update(self):
        """Обновление метки."""
        response = self.client.post(
            reverse("label_update", args=[self.label.pk]),
            {"name": "Обновлённая метка"},
        )
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, "Обновлённая метка")

    def test_label_delete(self):
        """Удаление метки."""
        response = self.client.post(
            reverse("label_delete", args=[self.label.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(name="Тестовая метка").exists())

    def test_label_delete_with_task(self):
        """Нельзя удалить метку, связанную с задачей."""
        # Создаём задачу с меткой
        task = Task.objects.create(
            name="Тестовая задача", status=self.status, author=self.user
        )
        task.labels.add(self.label)

        # Пытаемся удалить метку
        response = self.client.post(
            reverse("label_delete", args=[self.label.pk])
        )
        self.assertEqual(response.status_code, 302)  # редирект
        self.assertTrue(
            Label.objects.filter(name="Тестовая метка").exists()
        )  # метка не удалена
