from allauth.account.adapter import DefaultAccountAdapter
from .site import CURRENT_SITE


class DefaultAccountAdapterCustom(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = CURRENT_SITE + \
            '/verify-email/' + context['key'] + '/'
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
