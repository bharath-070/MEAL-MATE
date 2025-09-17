from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('open_signin/', views.open_signin, name='open_signin'),
    path('open_signup/', views.open_signup, name='open_signup'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('signin/open_add_restaurant', views.open_add_restaurant, name = 'open_add_restaurant'),
    path('signin/open_show_restaurant', views.open_show_restaurant, name = 'open_show_restaurant'),
    path('add_restaurant', views.add_restaurant, name='add_restaurant'),
]


#https://github.com/Gamana/MealMatebuddy
#https://github.com/Gamana/Practicemealmate