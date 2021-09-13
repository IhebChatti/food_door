from django.db import models


FOOD_TYPES = (
    ('appetizer', 'appetizer'),
    ('entree', 'entree'),
    ('dessert', 'dessert'),
)

class Restaurant(models.Model):
    name            = models.CharField(max_length=254, null=False)
    description     = models.CharField(max_length=254)
    image           = models.ImageField(upload_to='restaurant')
    phone           = models.CharField(max_length=254)
    address         = models.CharField(max_length=254)
    
    class Meta(object):
        db_table = 'restaurant'
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'


class FoodItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=FOOD_TYPES)

    class Meta(object):
        db_table = 'food_item'
        verbose_name = 'food_item'
        verbose_name_plural = 'food_items'

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