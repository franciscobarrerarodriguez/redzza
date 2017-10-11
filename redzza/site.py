from django.contrib.sites.models import Site
from .settings import DEBUG

try:
    if DEBUG:
        S3 = 'http://%s' % (Site.objects.get(id=8).domain)
        CURRENT_SITE = 'http://%s' % (Site.objects.get(id=5).domain)
        CURRENT_SITE_FRONTEND = 'http://%s' % (Site.objects.get(id=6).domain)
    else:
        S3 = 'http://%s' % (Site.objects.get(id=8).domain)
        CURRENT_SITE = 'http://%s' % (Site.objects.get(id=5).domain)
        CURRENT_SITE_FRONTEND = 'http://%s' % (Site.objects.get(id=7).domain)
except Exception as e:
    S3 = 'http://%s' % ('redzza.com')
    CURRENT_SITE = 'http://%s' % ('redzza.com')
    CURRENT_SITE_FRONTEND = 'http://%s' % ('redzza.com')
