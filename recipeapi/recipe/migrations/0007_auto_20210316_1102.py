# Generated by Django 3.1.7 on 2021-03-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_recipefood_recipeingredient1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipefood',
            name='recipeimage',
            field=models.ImageField(blank=True, null=True, upload_to='imagerecipe/'),
        ),
    ]