from django import forms
from django.contrib.auth.models import User
from societysearch.models import generalUserProfile, societyAdminUserProfile

class generalUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
    model = generalUser
    fields = ('username', 'email', 'password', 'university')


class societyAdminUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
    model = societyAdminUser
    fields = ('username', 'email', 'password', 'university', 'society name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = generalUserProfile
        fields = ( 'picture',)
