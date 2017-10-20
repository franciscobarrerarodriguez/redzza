from allauth.account.adapter import get_adapter as get_account_adapter
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email, user_field, user_username
from allauth.utils import valid_email_or_none
from .site import CURRENT_SITE_FRONTEND
from redzza import utils
from profiles.models import Profile, Place


class DefaultAccountAdapterCustom(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = CURRENT_SITE_FRONTEND + \
            '/verify-email/' + context['key'] + '/'
        msg = self.render_mail(template_prefix, email, context)
        msg.send()


class DefaultSocialAccountAdapterCustom(DefaultSocialAccountAdapter):

    def populate_user(self,
                      request,
                      sociallogin,
                      data):
        """
        Hook that can be used to further populate the user instance.
        For convenience, we populate several common fields.
        Note that the user instance being populated represents a
        suggested User instance that represents the social user that is
        in the process of being logged in.
        The User instance need not be completely valid and conflict
        free. For example, verifying whether or not the username
        already exists, is not a responsibility.
        """
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        name = data.get('name')
        user = sociallogin.user
        user_email(user, valid_email_or_none(email) or '')
        name_parts = (name or '').partition(' ')
        user_field(user, 'first_name', first_name or name_parts[0])
        user_field(user, 'last_name', last_name or name_parts[2])
        username = utils.generateRandomUsername(first_name or name_parts[0] or '')
        user_username(user, username)
        return user
