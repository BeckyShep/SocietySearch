from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import datetime


from societysearch.forms import GeneralSignUpForm, SocietyAdminSignUpForm, GeneralProfileForm, SocietyAdminProfileForm
from societysearch.models import User, GeneralUserProfile, SocietyAdminUserProfile
# Create your views here.

# Index page
def index(request):
    return render(request, 'societysearch/index.html')

# About page
def about(request):
    return render(request, 'societysearch/about.html')

def account_page(request):
    user_form = GeneralSignUpForm()
    profile_form = GeneralProfileForm()

    return render(request, 'account/account_page.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registerd': True})

def GeneralSignUpView(request):
    registered = False

    if request.method == "POST":
        user_form = GeneralSignUpForm(request.POST)
        profile_form = GeneralProfileForm(request.POST)
         
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
         user_form = GeneralSignUpForm()
         profile_form = GeneralProfileForm()

    return render(request, 'registration/generalsignup.html',
                  context = {'user_form':user_form,
                             'profile_form':profile_form,
                             'registerd':registered})


def SocietyAdminSignUpView(request):
     registered = False

     if request.method == "POST":
         user_form = SocietyAdminSignUpForm(request.POST)
         profile_form = SocietyAdminProfileForm(request.POST)

         if user_form.is_valid() and profile_form.is_valid():
             user = user_form.save
             user.set_password(user.password)
             user.save()

             profile = profile_form.save(commit=False)
             profile.user = user

             if 'picture' in request.FILES:
                 profile.picture = request.FILES['picture']

             profile.save()

             registered = True

         else:
             print(user_form.errors, profile_form.errors)

     else:
         user_form = SocietyAdminSignUpForm()
         profile_form = SocietyAdminProfileForm()

     return render(request, 'registration/societyadminsignup.html',
                   context = {'user_form':user_form, 'profile_form': profile_form, 'registerd': registered})


