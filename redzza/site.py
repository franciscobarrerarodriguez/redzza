from django.contrib.sites.models import Site
from .settings import DEBUG

try:
    if DEBUG:
        CURRENT_SITE = 'http://%s' % (Site.objects.get(id=5).domain)
        CURRENT_SITE_FRONTEND = 'http://%s' % (Site.objects.get(id=6).domain)
    else:
        CURRENT_SITE = 'http://%s' % (Site.objects.get(id=5).domain)
        CURRENT_SITE_FRONTEND = 'http://%s' % (Site.objects.get(id=7).domain)
except Exception as e:
    CURRENT_SITE = 'http://%s' % ('redzza.com')
    CURRENT_SITE_FRONTEND = 'http://%s' % ('redzza.com')
