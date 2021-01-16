from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contact-us/', views.contact_us,name='contact_us'),
    path('committee/', views.committee,name='committee')
]