from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a superuser with username=admin and password=admin"

    def handle(self, *args, **options):
        # Check if the 'admin' user already exists
        if User.objects.filter(username="admin").exists():
            self.stdout.write(
                self.style.SUCCESS('Superuser with username "admin" already exists.')
            )
        else:
            # Create the superuser
            User.objects.create_superuser("admin", "admin@example.com", "admin")
            self.stdout.write(
                self.style.SUCCESS(
                    'Superuser with username "admin" created successfully.'
                )
            )
