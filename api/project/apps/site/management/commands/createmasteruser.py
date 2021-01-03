from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from util import check_envv_exists_and_get


class Command(BaseCommand):

    def handle(self, *args, **options):

        master_username = check_envv_exists_and_get('MASTER_USERNAME')
        master_email = check_envv_exists_and_get('MASTER_EMAIL')
        master_password = check_envv_exists_and_get('MASTER_PASSWORD')

        if master_username is None or master_email is None or master_password is None:
            return

        User = get_user_model()
        if not User.objects.filter(username=master_username).exists():
            User.objects.create_superuser(username=master_username, email=master_email, password=master_password)
