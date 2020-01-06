from django.shortcuts import render
from .models import *

# Create your views here.


def login(request):
    print(request)
    if request.method=="POST":
        print("its a post method")
        firstname=request.POST["firstname"]
        password=request.POST["pwd"]
        print(firstname, password)
    return render(request,'login.html')


def registration(request):
    print(request)
    if request.method=="POST":
        print("its a post method")
        student_object = studentinfo.objects.create()
        student_object["firstname"] = request.POST["firstname"]
        student_object["lsatname"] = request.POST["lastname"]
        student_object["email"] = request.POST["email"]
        student_object["password"] = request.POST["password"]
        student_object["dob"] = request.POST["birthday"]
        student_object["gender"] = request.POST["Gender"]
        print("student_object before")
        student_object.save()
        print("student_object after")

    return render(request,'registration.html')


def markslist(request):
    return render(request,'markslist.html')

def marksview(request):
    return render(request,'marksview.html')
