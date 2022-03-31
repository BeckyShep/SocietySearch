from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class GeneralUserProfile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     
     is_general = models.BooleanField(default=True)
     is_societyAdmin = models.BooleanField(default=False)
     university = models.CharField(blank=False, max_length=40)
     picture = models.ImageField(upload_to='profile_images', blank=True)

     def __str__(self):
         return self.user.username

class SocietyAdminUserProfile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     
     is_societyAdmin = models.BooleanField(default=True)
     is_general = models.BooleanField(default=False)
     society= models.CharField(blank=False, max_length=40)
     university = models.CharField(blank=False, max_length=40)
     facebook = models.URLField(blank = True)
     discord = models.URLField(blank = True)
     twitter = models.URLField(blank = True)
     instagram = models.URLField(blank = True)
     picture = models.ImageField(upload_to='profile_images', blank=True)

     def __str__(self):
         return self.user.username
