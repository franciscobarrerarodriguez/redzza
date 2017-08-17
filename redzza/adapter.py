from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.sites.models import Site


class DefaultAccountAdapterCustom(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        current_site = Site.objects.get_current()
        context['activate_url'] = 'http://%s/' % (current_site.domain) + \
            'verify-email/' + context['key'] + '/'
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
