from django import forms
from django.contrib.auth.models import User
from societysearch.models import GeneralUserProfile, SocietyAdminUserProfile, User, SocietyPage, Reviews

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
          fields = ('picture',)


class SocietyForm(forms.ModelForm):
    name = forms.CharField(max_length=32, help_text="Name of Society:")
    twitter = forms.URLField(max_length=200, help_text="Twitter URL:")
    facebook = forms.URLField(max_length=200, help_text="Facebook URL:")
    discord = forms.URLField(max_length=200, help_text="Discord URL:")
    availability = forms.CharField(max_length=100,help_text="What is the availability of joining?")
    nextEvent = forms.CharField(max_length=200,help_text="When is the next event?")
    description = forms.CharField(max_length=500,help_text="Description of Society:")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = SocietyPage
        fields = ('name','facebook','discord','twitter','availability','nextEvent','description')




class ReviewForm(forms.ModelForm):
    review = forms.CharField(max_length=300,help_text="Please Enter your review of the Society:")

    class Meta:
        model = Reviews
        exclude = ('society','date','likes')


class SocietyAdminProfileForm(forms.ModelForm):
     class Meta:
         model = SocietyAdminUserProfile
         fields = ('society', 'university', 'facebook', 'discord', 'twitter', 'instagram', 'picture',)
