from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home),
    path('contact', views.Contact ),
    path('about', views.About ),
    path('signup', views.handleSignUp),
    path('login', views.handlelogin),
    path('logout', views.handlelogout),
    
]
