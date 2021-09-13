from django.contrib import admin
from restaurant.models import RestaurantImage, Restaurant, FoodItem, Menu

admin.site.register(RestaurantImage)
admin.site.register(Restaurant)
admin.site.register(FoodItem)
admin.site.register(Menu)