from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
     is_general = models.BooleanField(default=False)
     is_societyAdmin = models.BooleanField(default=False)

class GeneralUserProfile(models.Model):
     generalUser = models.OneToOneField(User, on_delete=models.CASCADE)
     username = models.CharField(blank=False, max_length=40)
     email = models.EmailField(blank=False)
     university = models.CharField(blank=False, max_length=40)
     picture = models.ImageField(upload_to='profile_images', blank=True)

     def __str__(self):
         return self.GeneralUser.username

class SocietyAdminUserProfile(models.Model):
     societyAdminUser = models.OneToOneField(User, on_delete=models.CASCADE)
     username = models.CharField(blank=False, max_length=40)
     society= models.CharField(blank=False, max_length=40)
     university = models.CharField(blank=False, max_length=40)
     email = models.EmailField(blank=False)
     facebook = models.URLField(blank = True)
     discord = models.URLField(blank = True)
     twitter = models.URLField(blank = True)
     instagram = models.URLField(blank = True)
     picture = models.ImageField(upload_to='profile_images', blank=True)

     def __str__(self):
         return self.SocietyAdminUser.username
