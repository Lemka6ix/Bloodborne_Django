from django.db import models
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    short_content = models.TextField(verbose_name='Краткое содержание')
    content = models.TextField(verbose_name='Полное содержание')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')

    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    verbose_name='Автор статьи')

    image = models.ImageField(
    upload_to='blog/',
    blank=True,
    null=True,
    verbose_name='Изображение статьи')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    post = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Статья'
    )

    def __str__(self):
        return f'Комментарий от {self.author} к статье {self.post}'