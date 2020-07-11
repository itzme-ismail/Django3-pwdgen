from django.shortcuts import render
from django.urls import path
from gen import views

urlpatterns = [
    path('',views.home,name='home'),
    path('pwd',views.pwd),
    path('about',views.about,name='about'),
]
