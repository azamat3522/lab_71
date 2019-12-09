from django.db import models

QUOTE_NEW = 'new'
QUOTE_APPROOVED = 'approved'

QUOTE_STATUS_CHOICES = (
    (QUOTE_NEW, 'Новая'),
    (QUOTE_APPROOVED, 'Проверена')
)


class Quote(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Teкст цитаты')
    author_name = models.CharField(max_length=30, verbose_name='Имя автора')
    author_email = models.EmailField(verbose_name='Email')
    status = models.CharField(max_length=20, choices=QUOTE_STATUS_CHOICES, default=QUOTE_NEW, verbose_name='Статус')
    rating = models.IntegerField(default=0, verbose_name='Рэйтинг')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.text[:20] + "..."

    class Meta:
        verbose_name = 'Цитата'
        verbose_name = 'Цитаты'
