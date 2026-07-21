from django.contrib.auth.models import User
from django.db import models

from labels.models import Label
from statuses.models import Status


class Task(models.Model):
    """Модель задачи."""

    name = models.CharField(max_length=150, unique=True, verbose_name="Имя")
    description = models.TextField(blank=True, verbose_name="Описание")
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name="Статус"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="tasks_author",
        verbose_name="Автор",
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks_executor",
        verbose_name="Исполнитель",
    )
    labels = models.ManyToManyField(
        Label, blank=True, related_name="tasks", verbose_name="Метки"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
