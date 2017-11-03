from rest_auth.serializers import PasswordResetSerializer
from rest_auth.models import TokenModel
from rest_framework import serializers
from django.core import serializers as djangoSerializers
from redzza import utils
import json
from .site import CURRENT_SITE_FRONTEND
from profiles.models import Profile


class CustomTokenSerializer(serializers.ModelSerializer):
    """
    Custom Serializer for Token model.
    """
    data = serializers.SerializerMethodField()

    def get_data(self, obj):
        user = obj.user
        token = utils.getToken(user)
        timeToken = utils.getTimeToken(token)
        userSerialized = json.loads(djangoSerializers.serialize('json', [user], fields=('username', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined')))
        if user.is_staff:
            return {'success': True, 'msg': 'user-admin', 'user': userSerialized, 'token': token.key, 'timeToken': timeToken}
        else:
            return {'success': True, 'msg': 'user-normal', 'user': userSerialized, 'token': token.key, 'timeToken': timeToken}

    class Meta:
        model = TokenModel
        fields = ('data',)


class CustomPasswordResetSerializer(PasswordResetSerializer):

    def get_email_options(self):
        return {'extra_email_context': {'CURRENT_SITE_FRONTEND': CURRENT_SITE_FRONTEND}}

    def validate_email(self, value):
        if not Profile.searchEmail(value):
            raise serializers.ValidationError('non-existent')

        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return value
