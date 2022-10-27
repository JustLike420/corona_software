from django.db import models

# Create your models here.
from django.urls import reverse

CATEGORIES_CHOICE = (
    ('Game', 'Game'),
    ('Soft', 'Soft'),
    ('Plugin', 'Plugin'),

)


class Posts(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICE, verbose_name='Раздел')
    details = models.TextField(max_length=1000, verbose_name='Описание')
    description = models.TextField(max_length=1000, verbose_name='Системные требования')
    photo = models.ImageField(blank=True, default='photo.png')
    file = models.FileField()
    sub_title = models.CharField(max_length=100, verbose_name='Компания')

    def __str__(self):
        return f'{self.category} | {self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

