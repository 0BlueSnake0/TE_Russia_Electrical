from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    slug = models.SlugField(default='', max_length=255, unique=True, verbose_name="Slug")
    title = models.CharField(default='',max_length=255, verbose_name="Заголовок", blank=True)
    file = models.FileField(
        default='',upload_to='videos',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])], 
        verbose_name="Файл",
    ) 
    preview = models.ImageField(default='', upload_to='images/previews', verbose_name="Превью")
    description = RichTextUploadingField(default='',blank=True, verbose_name="Описание")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return self.title