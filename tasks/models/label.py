from django.db import models


class Label(models.Model):
    """Модель метки (тега) для задач."""
    name = models.CharField(max_length=150, unique=True, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'
