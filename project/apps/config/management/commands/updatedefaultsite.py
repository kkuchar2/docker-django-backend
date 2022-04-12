from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Updating Site')

        site_id = settings.SITE_ID
        production_env = settings.PRODUCTION_ENV
        host = "api.kkucharski.com" if production_env else "0.0.0.0"

        print("Site ID: {}, production env: {}, host: {}".format(site_id, production_env, host))

        if Site.objects.filter(pk=site_id).exists():
            print('Site of id: {} already exists, updating.'.format(site_id))
            site = Site.objects.get(pk=site_id)
            site.domain = host
            site.name = host
            site.save()
        else:
            print('Site of id: {} does not exist, creating.')
            Site(pk=site_id, domain=host, name=host).save()
