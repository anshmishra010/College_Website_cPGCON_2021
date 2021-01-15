from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.call_for_paper ,name='home'),
]