# Generated by Django 4.1.3 on 2022-11-13 00:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_remove_recipecollection_create_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeCollection',
            new_name='MealPlans',
        ),
    ]
