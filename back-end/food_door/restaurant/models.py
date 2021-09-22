from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db.models.fields import related

fs = FileSystemStorage(location='/media/photos')


class Restaurant(models.Model):
    name            = models.CharField(max_length=254, null=False)
    description     = models.CharField(max_length=254)
    phone           = models.CharField(max_length=254)
    address         = models.CharField(max_length=254)
    
    class Meta(object):
        db_table = 'restaurant'
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

def nameFile(instance, filename):
    return '/'.join(['media', str(instance.name), filename])

class RestaurantImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField(null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="images")
    
    class Meta(object):
        db_table = 'restaurant_image'
        verbose_name = 'restaurant_image'
        verbose_name_plural = 'restaurant_images'


class FoodItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant")

    class Meta(object):
        db_table = 'food_item'
        verbose_name = 'food_item'
        verbose_name_plural = 'food_items'


class FoodImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="images")
    
    class Meta(object):
        db_table = 'food_image'
        verbose_name = 'food_image'
        verbose_name_plural = 'food_images'

class Menu(models.Model):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    food_items = models.ManyToManyField(FoodItem)
    
    class Meta(object):
        db_table = 'menu'
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
