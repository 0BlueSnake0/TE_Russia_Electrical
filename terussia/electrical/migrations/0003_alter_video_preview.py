# Generated by Django 3.2.7 on 2021-11-04 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrical', '0002_alter_video_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='preview',
            field=models.ImageField(blank=True, default='', upload_to='electrical/images/previews'),
        ),
    ]
