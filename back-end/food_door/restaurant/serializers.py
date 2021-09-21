from rest_framework import serializers
from restaurant.models import FoodItem, Restaurant, RestaurantImage, FoodImage
from django.core import exceptions
import django.contrib.auth.password_validation as validators

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'description', 'phone', 'address', 'images')
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'name', 'description', 'price')

class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        fields = ('id', 'name', 'image')