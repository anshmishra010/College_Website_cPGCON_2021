from django.shortcuts import render

def call_for_paper(request, *args, **kwargs) :
    return render(request,'call_for_paper.html', {})


# Create your views here.
