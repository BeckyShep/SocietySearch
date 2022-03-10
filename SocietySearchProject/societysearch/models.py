from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_general = models.BooleanField(default=False)
    is_societyAdmin = models.BooleanField(default=False)

class generalUserProfile(models.Model):
    generalUser = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CHARField(blank=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.generalUser.username

class societyAdminUserProfile(models.Model):
    societyAdminUser = models.OneToOneField(User, on_delete=models.CASCADE)
    
    email = models.CHARField(blank=False)
    facebook = models.URLField(blank = True)
    discord = models.URLField(blank = True)
    twitter = models.URLField(blank = True)
    instagram = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.societyAdminUser.username
