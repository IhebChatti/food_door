# Generated by Django 3.2.7 on 2021-09-10 17:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='email address')),
                ('username', models.CharField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='user email address')),
                ('password', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
    ]
