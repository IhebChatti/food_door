from rest_framework import serializers
from restaurant.models import Restaurant, RestaurantImage
from django.core import exceptions
import django.contrib.auth.password_validation as validators

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'description', 'phone', 'address', 'image')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ('name', 'image')
