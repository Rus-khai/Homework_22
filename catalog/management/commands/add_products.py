from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add products from JSON file"

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_1, _ = Category.objects.get_or_create(
            name="Фрукты", description="Здесь находятся все фрукты"
        )
        category_2, _ = Category.objects.get_or_create(
            name="Овощи", description="Здесь находятся все овощи"
        )

        products = [
            {
                "name": "Манго",
                "description": "Манго очень полезный фрукт",
                "price": 50.00,
                "category": category_1,
            },
            {
                "name": "Апельсин",
                "description": "Апельсин очень полезный фрукт",
                "price": 40.00,
                "category": category_1,
            },
            {
                "name": "Картофель",
                "description": "Картофель очень полезный овощ",
                "price": 30.00,
                "category": category_2,
            },
            {
                "name": "Репа",
                "description": "Репа очень полезный овощ",
                "price": 50.00,
                "category": category_2,
            },
        ]
        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Product '{product.name}' created")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product '{product.name}' already exists")
                )
