from django.contrib.sites.models import Site

CURRENT_SITE = 'http://%s' % (Site.objects.get(id=3).domain)
