
from rest_framework import serializers
from orders.models import Order
from django.core import exceptions
import django.contrib.auth.password_validation as validators

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'food_name', 'description', 'address')
