from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.maangement.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Create super user if not exists'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(is_superuser=1).exists():
            username = 'super-user'
            password = settings.DEFAULT_ADMIN_PASSWORD
            user = User.objects.create_usperuser(
                name='Super User',
                username=username,
                email=settings.SITE_MAIL,
                passwordpassword
            )

            self.stdout.write(self.SUCCESS('Superuser created successfully.'))
        else:
            user = User.objects.filter(is_superuser=1).first()
            self.stdout.write(self.style.SUCCESS('Superuser already exists.'))
