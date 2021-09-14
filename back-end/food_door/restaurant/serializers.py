from rest_framework import serializers
from restaurant.models import Restaurant, RestaurantImage
from django.core import exceptions
import django.contrib.auth.password_validation as validators

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'description', 'phone', 'address')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ('id', 'name', 'image')
