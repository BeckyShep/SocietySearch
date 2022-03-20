from django import forms
from django.contrib.auth.models import User
from societysearch.models import GeneralUserProfile, SocietyAdminUserProfile, User

class GeneralSignUpForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
    
     class Meta:
          model = GeneralUserProfile
          fields = ('username', 'email', 'password', 'university')


class SocietyAdminSignUpForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
    
     class Meta:
          model = SocietyAdminUserProfile
          fields = ('username', 'email', 'password', 'university', 'society')

class GeneralProfileForm(forms.ModelForm):
     class Meta:
         model = GeneralUserProfile
         fields = ('picture',)

class SocietyAdminProfileForm(forms.ModelForm):
     class Meta:
         model = SocietyAdminUserProfile
         fields = ('picture',)
