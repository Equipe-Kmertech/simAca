from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def courses(request):
    return render(request, "courses.html")

def about(request):
    return render(request, "about.html")

def details(request):
    return render(request, "details.html")