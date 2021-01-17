from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_us(request, *args, **kwargs):
    return render(request, "contact_us.html", {})

def committee(request, *args, **kwargs):
    return render(request, "committee.html", {})

def important_dates(request, *args, **kwargs):
    return render(request, "important_dates.html", {})

def registration(request, *args, **kwargs):
    return render(request, "registration.html", {})