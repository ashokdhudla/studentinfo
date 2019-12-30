from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def markslist(request):
    return render(request,'markslist.html')
