from django.shortcuts import render
from .models import *

# Create your views here.


def login(request):
    print(request)
    if request.method == "POST":
        print("its a post method")
        email = request.POST["email"]
        password = request.POST["pwd"]
        student_object = studentinfo.objects.filter(email=email, password=password)
        if student_object:
            print("email and password")
        else:
            print("invalid emil or password")
    return render(request, 'login.html')


def registration(request):
    print(request)
    if request.method == "POST":
        print("its a post method")
        student_object = studentinfo.objects.create()
        student_object.firstname = request.POST["firstname"]
        student_object.lastname = request.POST["lastname"]
        student_object.email = request.POST["email"]
        student_object.password = request.POST["password"]
        student_object.dob = request.POST["birthday"]
        student_object.gender = request.POST["gender"]
        print("student_object before")
        student_object.save()
        print("student_object after")

    return render(request, 'registration.html')


def markslist(request):
    return render(request, 'markslist.html')


def marksview(request):
    return render(request, 'marksview.html')

def StuMarks(request):
    print(request)
    if request.method == "POST":
        print("its a post method")
        student_object = addmarks.objects.create()
        student_object.id_no = request.POST["id_no"]
        student_object.firstname = request.POST["firstname"]
        student_object.lastname = request.POST["lastname"]
        student_object.dateofexam = request.POST["dateofexam"]
        student_object.maths = request.POST["maths"]
        student_object.physics = request.POST["physics"]
        student_object.chemistry = request.POST["chemistry"]
        print("student_object before")
        student_object.save()
        print("student_object after")

    return render(request, 'addmarks.html')
