# Generated by Django 3.2.7 on 2021-11-04 14:07

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', max_length=255, unique=True)),
                ('title', models.CharField(default='', max_length=255, verbose_name='Title')),
                ('file', models.FileField(default='', upload_to='electrical/videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='File')),
                ('preview', models.ImageField(default='electrical/images/previews', upload_to='')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Description')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
