"""SocietySearchProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from societysearch import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'societysearch'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('societysearch/', include(('societysearch.urls', 'societysearch'), namespace='societysearch')),
    path('admin/', admin.site.urls),
    path('search/', views.search, name='search'),
    path('add_society', views.add_society, name='add_society'),
    path('search/society/<slug:society_name_slug>/', views.show_society, name='show_society'),
    path('search/society/<slug:society_name_slug>/add_review', views.add_review, name='add_review'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/register/generalsignup/', views.GeneralSignUpView, name = 'GeneralSignUp'),
    path('accounts/register/societyadminsignup/', views.SocietyAdminSignUpView, name = 'SocietyAdminSignUp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

