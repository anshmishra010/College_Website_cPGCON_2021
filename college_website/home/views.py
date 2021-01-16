from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_us(request, *args, **kwargs):
    return render(request, "contact_us.html", {})

def committee(request, *args, **kwargs):
    return render(request, "committee.html", {})