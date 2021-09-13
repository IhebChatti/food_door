# Generated by Django 3.2.7 on 2021-09-13 14:20

from django.db import migrations, models
import django.db.models.deletion
import restaurant.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_restaurant_image'),
    ]

    operations = [
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
    ]