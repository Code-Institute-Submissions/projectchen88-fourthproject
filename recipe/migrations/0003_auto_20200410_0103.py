# Generated by Django 2.2.4 on 2020-04-10 01:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0002_remove_recipe_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='recipe',
            new_name='Dish',
        ),
    ]
