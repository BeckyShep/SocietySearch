from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime

from societysearch.forms import GeneralSignUpForm, SocietyAdminSignUpForm
from societysearch.models import User

# Create your views here.


def GeneralSignUpView(request):
    registered = False

    if request.emthod == "Post":
        user_form = GeneralSignUpForm(request.Post)
        profile_form = GeneralProfileForm(request.Post)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save
            
            user.is_general = True
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.Files:
                profile.picture = request.Files['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = GeneralSignUpForm()
        profile_form = GeneralProfileForm()

    return render(request, 'societysearch/signup/general',
                  context = {'user_form' = user_form, 'profile_form': profile_form, 'registerd': registered})


def SocietyAdminSignUpView(request):
    registered = False

    if request.emthod == "Post":
        user_form = SocietyAdminSignUpForm(request.Post)
        profile_form = SocietyAdminProfileForm(request.Post)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save
            
            user.is_societyAdmin = True
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.Files:
                profile.picture = request.Files['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = SocietyAdminSignUpForm()
        profile_form = SocietyAdminProfileForm()

    return render(request, 'societysearch/signup/societyadmin',
                  context = {'user_form' = user_form, 'profile_form': profile_form, 'registerd': registered})


