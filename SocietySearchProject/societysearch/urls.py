from django.urls import path
from societysearch import views

app_name = 'societysearch'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),

]
