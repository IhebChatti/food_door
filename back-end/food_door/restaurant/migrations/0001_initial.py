# Generated by Django 3.2.7 on 2021-09-19 17:15

from django.db import migrations, models
import django.db.models.deletion
import restaurant.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=100)),
            ],
            options={
                'verbose_name': 'food_item',
                'verbose_name_plural': 'food_items',
                'db_table': 'food_item',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name': 'restaurant',
                'verbose_name_plural': 'restaurants',
                'db_table': 'restaurant',
            },
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=restaurant.models.nameFile)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='restaurant.restaurant')),
            ],
            options={
                'verbose_name': 'restaurant_image',
                'verbose_name_plural': 'restaurant_images',
                'db_table': 'restaurant_image',
            },
        ),
        migrations.CreateModel(
            name='FoodImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=restaurant.models.nameFile)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='restaurant.fooditem')),
            ],
            options={
                'verbose_name': 'food_image',
                'verbose_name_plural': 'food_images',
                'db_table': 'food_image',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='restaurant.restaurant')),
                ('food_items', models.ManyToManyField(to='restaurant.FoodItem')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menus',
                'db_table': 'menu',
            },
        ),
    ]
