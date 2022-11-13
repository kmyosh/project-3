# Generated by Django 4.1.3 on 2022-11-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_recipecollection_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipecollection',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='recipecollection',
            name='recipe_id',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='name',
        ),
        migrations.AddField(
            model_name='recipecollection',
            name='recipes',
            field=models.ManyToManyField(to='main_app.recipes'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='recipe_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
