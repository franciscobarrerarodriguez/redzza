from django.contrib.sites.models import Site

try:
    CURRENT_SITE = 'http://%s' % (Site.objects.get(id=5).domain)
    CURRENT_SITE_FRONTEND = 'http://%s' % (Site.objects.get(id=6).domain)
except Exception as e:
    CURRENT_SITE = 'http://%s' % ('redzza.com')
    CURRENT_SITE_FRONTEND = 'http://%s' % ('redzza.com')
