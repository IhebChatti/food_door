from rest_framework import serializers
from users.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'address')
