# Generated by Django 3.2.7 on 2021-11-03 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211103_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registered_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Registration date'),
        ),
    ]
