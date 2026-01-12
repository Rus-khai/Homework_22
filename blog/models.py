from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    content = models.TextField(
        verbose_name="Содержание", help_text="Введите содержание"
    )
    preview = models.ImageField(
        upload_to="blog/previews/",
        verbose_name="Предварительный просмотр",
        help_text="Загрузите предварительный просмотр",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания записи",
    )
    published = models.BooleanField(
        default=False,
        verbose_name="Не опубликовано",
        help_text="Отметьте, если запись опубликована",
    )
    count_views = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created_at"]
