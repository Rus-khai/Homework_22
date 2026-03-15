from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Удаление пользователя'

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.get(email='ruselkotya@gmail.com')
        user.delete()
