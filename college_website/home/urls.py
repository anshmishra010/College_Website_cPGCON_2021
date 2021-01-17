from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contact-us/', views.contact_us,name='contact_us'),
    path('committee/', views.committee,name='committee'),
    path('important-dates/', views.important_dates ,name='important_dates'),
    path('registration/', views.registration ,name='registration'),
    path('venue/', views.venue ,name='venue')
]