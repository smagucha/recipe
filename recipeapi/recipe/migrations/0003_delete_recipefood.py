# Generated by Django 3.1.6 on 2021-03-15 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20210315_1759'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecipeFood',
        ),
    ]