from django.contrib.auth.management.commands import createsuperuser
from django.contrib.auth.models import User


class Command(createsuperuser.Command):

    def remove_old_superuser(self):
        user = User.objects.get(username="root")
        if user is not None:
            user.delete()

    def handle(self, *args, **options):
        self.remove_old_superuser()

        options['username'] = 'root'
        options['email'] = 'root@root.com'

        super(Command, self).handle(*args, **options)

        user = User.objects.get(username="root")
        user.set_password("root")
        user.save()
