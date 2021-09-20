from django.db import models

############### User model ##############
class Order(models.Model):
    food_name      = models.CharField(max_length=254, null=False)
    description    = models.CharField(max_length=254)
    address        = models.CharField(max_length=254)
    

    class Meta(object):
        db_table            = 'order'
        verbose_name        = 'Order'
        verbose_name_plural = 'Orders'

