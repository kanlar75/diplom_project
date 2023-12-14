from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='название',
                             **NULLABLE)
    price = models.IntegerField(verbose_name='цена', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='ads/', verbose_name='изображение',
                              **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name='пользователь', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='время публикации',
                                      **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ['-created_at']


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name='комментатор', **NULLABLE)
    text = models.TextField(verbose_name='отзыв')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE,
                           related_name='comment',
                           verbose_name='объявление', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='время публикации')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
