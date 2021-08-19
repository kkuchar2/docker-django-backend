from django.conf import settings
from django.contrib.sites.models import Site


class DynamicSiteDomainMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        current_site = None

        try:
            current_site = Site.objects.get(domain=request.get_host())
        except Site.DoesNotExist:

            try:
                current_site = Site.objects.get(id=settings.DEFAULT_SITE_ID)
            except Site.DoesNotExist:
                pass

        print(current_site)

        if current_site is not None:
            request.current_site = current_site
            settings.SITE_ID = current_site.id
        else:
            settings.SITE_ID = 1

        response = self.get_response(request)

        return response
