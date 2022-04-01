from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime


from societysearch.forms import SocietyForm, ReviewForm
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

@login_required
def account_page(request):
    return render(request, 'societysearch/account_page.html')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        societies = SocietyPage.objects.filter(name__contains=searched)
        return render(request, 'societysearch/search.html', {'searched': searched, 'societies': societies})
    else:
        return render(request, 'societysearch/search.html')

@login_required
def add_society(request):
    form = SocietyForm()

    if request.method == 'POST':
        form = SocietyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        else:
            print(form.errors)

    return render(request, 'societysearch/add_society.html', {'form': form})


def show_society(request, society_name_slug):
    context_dict = {}
    try:
        society = SocietyPage.objects.get(slug=society_name_slug)
        reviews = Reviews.objects.filter(society=society)
        context_dict['society'] = society
        context_dict['reviews'] = reviews

    except SocietyPage.DoesNotExist:
        context_dict['society'] = None
        ontext_dict['reviews'] = None

    return render(request, 'societysearch/society.html', context=context_dict)

@login_required
def add_review(request, society_name_slug):
    try:
        society = SocietyPage.objects.get(slug=society_name_slug)
    except SocietyPage.DoesNotExist:
        society = None

    if society is None:
        return redirect('index')

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if society:
                Reviews = form.save(commit=False)
                Reviews.society = society
                Reviews.date = datetime.date.today()
                Reviews.save()

                return redirect(reverse('show_society', kwargs={'society_name_slug': society_name_slug}))

        else:
            print(form.errors)

    context_dict = {'form':form,'society':society}
    return render(request,'societysearch/add_review.html',context=context_dict)

@login_required
def LikeView(request,id):
     review = get_object_or_404(Reviews, id=request.POST.get('review_id'))
     review.likes += 1
     return redirect(reverse('show_society', kwargs={'society_name_slug': review.society.slug}))

            
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

