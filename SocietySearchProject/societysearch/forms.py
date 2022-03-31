from django import forms
from django.contrib.auth.models import User
from societysearch.models import GeneralUserProfile, SocietyAdminUserProfile, User

class GeneralSignUpForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
    
     class Meta:
          model = User
          fields = ('username', 'email', 'password')


class SocietyAdminSignUpForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
    
     class Meta:
          model = User
          fields = ('username', 'email', 'password')

class GeneralProfileForm(forms.ModelForm):
     class Meta:
         model = GeneralUserProfile
         fields = ('university', 'picture',)

class SocietyAdminProfileForm(forms.ModelForm):
     class Meta:
         model = SocietyAdminUserProfile
         fields = ('society', 'university', 'facebook', 'discord', 'twitter', 'instagram', 'picture',)
