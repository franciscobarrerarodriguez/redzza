from rest_auth.serializers import PasswordResetSerializer
from rest_auth.models import TokenModel
from rest_framework import serializers
from django.core import serializers as djangoSerializers
from redzza import utils
import json
from .site import CURRENT_SITE_FRONTEND


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