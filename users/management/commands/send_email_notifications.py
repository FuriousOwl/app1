from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from users.models import User

class Command(BaseCommand):
    help = 'Send email notifications to users'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_active=True)
        for user in users:
            send_mail(
                'Notification Subject',
                'Here is the message.',
                'your-email@example.com',
                [user.email],
                fail_silently=False,
            )
        self.stdout.write(self.style.SUCCESS('Successfully sent notifications'))
