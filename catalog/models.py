from django.db import models

from config import settings


class Product(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="media/products/",
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория продукта",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name="Цена продукта",
        help_text="Введите цену продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания продукта"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата изменения продукта"
    )
    can_unpublish_product = models.BooleanField(default=False, verbose_name="Не разрешено отменить публикацию")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='object_list',
                              null=True,
                              blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]
        permissions = [
            ("can_unpublish_product", "Может отменить публикацию продукта"),
        ]


class Category(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
