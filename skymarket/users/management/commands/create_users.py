from django.core.management import BaseCommand

from users.models import User

values = ['admin', 'user1', 'user2', 'user3', 'user4']
domain = 'test.com'


class Command(BaseCommand):

    def handle(self, *args, **options):
        for value in values:
            if not User.objects.filter(email=value + '@' + domain).exists():
                user = User.objects.create(
                    email=value + '@' + domain,
                    first_name=value.title(),
                    last_name=value.title(),
                    is_superuser=True if value == 'admin' else False,
                    role='admin' if value == 'admin' else 'user',
                    is_staff=True if value == 'admin' else False,
                    is_active=True,
                )
                user.set_password('111')
                user.save()
            else:
                continue
