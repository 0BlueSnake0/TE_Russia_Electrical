from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator

from solo.models import SingletonModel
from phonenumber_field.modelfields import PhoneNumberField 


class Modal(models.Model):
    button_title = models.CharField(default='', max_length=255)
    button_text = models.TextField(default='', blank=True)
    slug = models.SlugField(default='', max_length=255, unique=True)
    content = RichTextUploadingField(default='', blank=True)


    def __str__(self):
        return f'{self.button_title}'


class Catalog(models.Model):
    name = models.CharField(default='', max_length=255)
    slug = models.SlugField(default='', max_length=255, unique=True)
    pdf = models.FileField(default='', upload_to='catalogs/', 
        validators=[
            FileExtensionValidator(['pdf'])
        ]
    )
    preview = models.ImageField(default='', blank=True, upload_to='catalog_previews/', 
        validators=[
            FileExtensionValidator(['png', 'jpg'])
        ] 
    )

    def __str__(self):
        return f'{self.name} ({self.slug})'


class ProductVideo(models.Model):
    title = models.CharField(default='', max_length=255)
    preview = models.ImageField(default='', blank=True, upload_to='catalog_previews/', 
        validators=[
            FileExtensionValidator(['png', 'jpg'])
        ] 
    )
    youtube_link = models.URLField(default='', max_length=255)


    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    name = models.CharField(default='', max_length=255)
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default='', max_length=255, unique=True)

    description1 = RichTextUploadingField(default='', blank=True)
    videos = models.ManyToManyField(ProductVideo, blank=True)
    description2 = RichTextUploadingField(default='', blank=True)
    modals = models.ManyToManyField(Modal, blank=True)
    description3 = RichTextUploadingField(default='', blank=True)
    catalogs = models.ManyToManyField(Catalog, blank=True)
    software_link = models.URLField(default='', blank=True, max_length=255)

    def __str__(self):
        return f'{self.name}' 


class Region(models.Model):
    name = models.CharField(default='', max_length=255, unique=True) 
    slug = models.SlugField(default='', max_length=255, unique=True)
    color= models.CharField(default='', max_length=255, unique=True)
    hover_color= models.CharField(default='', max_length=255, unique=True)


    def __str__(self):
        return f'{self.name}'


class State(models.Model):
    name = models.CharField(default='', max_length=255)
    slug = models.SlugField(default='', max_length=255, unique=True)
    region = models.ForeignKey(Region, default='', null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.name} ({self.slug})'

 
class ContactPerson(models.Model):
    first_name = models.CharField(default='', max_length=255)
    last_name = models.CharField(default='', max_length=255, unique=True)
    email = models.EmailField(default='', max_length=255, unique=True)
    tel = PhoneNumberField(default='')
    mobile = PhoneNumberField(default='', unique=True)
    extended_number = models.CharField(default='', max_length=255, blank=True)
    city = models.CharField(default='', max_length=255)


    position = models.CharField(default='', max_length=255)  
    organization = models.CharField(default='', max_length=255)  
    address = models.CharField(default='', max_length=255, blank=True)
    region = models.OneToOneField(Region, default='', null=True, on_delete=models.SET_NULL, unique=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class TimeTable(SingletonModel):
    table = models.FileField(default='', upload_to='timetables/', 
        validators=[
            FileExtensionValidator(['ods', 'xls', 'xlsx'])
        ] 
    )
