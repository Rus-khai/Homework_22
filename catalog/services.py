from catalog.models import Product
from django.core.cache import cache
from config.settings import CACHE_ENABLED
from django.shortcuts import get_object_or_404
from .models import Category, Product


def get_products_from_cache():
    """Получает все продукты из кеша или из базы данных, если кэш пустой."""

    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products"
    cached_data = cache.get(key)
    if cached_data is not None:
        return cached_data
    products = list(Product.objects.all())
    cache.set(key, products)
    return products


def get_products_by_category(category_slug):
    """Возвращает список всех продуктов по указанной категории."""

    # Получаем объект категории по слогу
    category = get_object_or_404(Category, slug=category_slug)

    # Получаем все продукты по этой категории
    products = Product.objects.filter(category=category)

    return products
