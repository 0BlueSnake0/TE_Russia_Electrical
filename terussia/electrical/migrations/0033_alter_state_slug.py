# Generated by Django 3.2.7 on 2022-07-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrical', '0032_alter_state_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]
