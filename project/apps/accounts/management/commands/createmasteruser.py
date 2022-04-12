from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from util import check_envv_exists_and_get


class Command(BaseCommand):

    def handle(self, *args, **options):

        master_email = check_envv_exists_and_get('MASTER_EMAIL')
        master_password = check_envv_exists_and_get('MASTER_PASSWORD')

        if master_email is None or master_password is None:
            return

        user_model = get_user_model()

        if not user_model.objects.filter(email=master_email).exists():
            user_model.objects.create_superuser(email=master_email, password=master_password)

        user = user_model.objects.get(email__exact=master_email)

        if not EmailAddress.objects.filter(email=master_email).exists():
            email_address = EmailAddress.objects.create(email=master_email, user=user)

        email_address = EmailAddress.objects.get(email__exact=master_email)
        email_address.verified = True
        email_address.primary = True
        email_address.save()




