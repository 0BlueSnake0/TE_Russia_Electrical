# Generated by Django 3.2.7 on 2022-07-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrical', '0022_alter_product_catalogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactperson',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
    ]
