# Generated by Django 3.2.7 on 2021-09-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]
