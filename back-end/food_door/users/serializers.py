from rest_framework import serializers
from users.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime, timedelta
from users.config import logger as ulm
import pytz
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True}
        }
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         tolerance = datetime.now(tz=pytz.utc) - timedelta(minutes = 10)
#         previous_attempts = ulm.UserLoginActivity.objects.filter(
#             login_username = self.initial_data['username'],
#             status='failed',
#             login_datetime__gt = tolerance,
#         ).count()
#         if previous_attempts < 3:
#             try:
#                 data = super().validate(attrs)
#                 refresh = super().get_token(self.user)
#                 data['refresh'] = str(refresh)
#                 data['access'] = str(refresh.access_token)
#                 # Add extra responses here
#                 ulm.log_user_logged_in_success(sender=self.user.__class__, request=self.context['request'], user=self.user)
#                 data['user_id'] = self.user.id
#                 data['user_type'] = self.user.roles_list()
#                 data['verified'] = self.user.is_verified
#                 return data
#             except Exception as ex:
#                 ulm.log_user_logged_in_failed(sender=self.user.__class__, request=self.context['request'], credentials=self.initial_data)
#                 return {'error': str(ex)}
#         else:
#             return {'error':'maximum attempts exceeded in the last 10 minutes'}
