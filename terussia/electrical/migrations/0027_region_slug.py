# Generated by Django 3.2.7 on 2022-07-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrical', '0026_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]