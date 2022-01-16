from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser 
import datetime
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, 
                    avatar=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have an email!')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.username = username
        user.is_admin = is_admin
        user.is_staff = is_staff 
        user.avatar = avatar
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, 
                         avatar=None, is_staff=True, is_admin=True):
        if not email:
            raise ValueError('Users must have an email!')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.username = username
        user.is_admin = is_admin
        user.is_staff = is_staff 
        user.avatar = avatar
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):  
    username = models.CharField(default='', max_length=30, unique=True, verbose_name='Username')
    avatar = models.ImageField(default=f'', upload_to='accounts/users/avatars',
                               blank=True, verbose_name='Avatar')
    password = models.CharField(default='', max_length=30, verbose_name='Password')
    email = models.EmailField(default='', max_length=30, verbose_name='Email')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    registered_at = models.DateTimeField(auto_now_add=True,editable=False,verbose_name='Registration date')
 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] 
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True 

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username