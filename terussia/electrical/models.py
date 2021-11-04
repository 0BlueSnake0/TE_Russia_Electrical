from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    slug = models.SlugField(default='', max_length=255, unique=True)
    title = models.CharField(default='',max_length=255, verbose_name="Title",)
    file = models.FileField(
        default='',upload_to='electrical/videos',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])], 
        verbose_name="File",
    )
    author = models.ForeignKey("accounts.User", default='', on_delete=models.PROTECT, verbose_name="Author")
    preview = models.ImageField(default='', upload_to='electrical/images/previews', blank=True)
    description =RichTextUploadingField(default='',blank=True, verbose_name="Description")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded")

    def __str__(self):
        return self.title