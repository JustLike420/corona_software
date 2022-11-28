from django.db import models
from PIL import Image
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
    file = models.FileField(default='setup.zip', null=True, blank=True)
    sub_title = models.CharField(max_length=100, verbose_name='Компания', default='password: coronasf', null=True,
                                 blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return f'{self.category} | {self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)

        img.thumbnail((474, 766))
        img.save(self.photo.path)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
