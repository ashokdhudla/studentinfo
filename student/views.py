from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        print("post method calling")
        email = request.POST['email']
        password = request.POST['pwd']
        student_object = studentinfo.objects.filter(email=email, password=password)
        if student_object:
            print("email and password")
            request.session["user"] = student_object[0].id
            return render(request, 'home.html', {"studentinfo": student_object[0]})
        else:
            print("invalid email or password")
            return render(request, 'login.html', {"error": "invalid email or password "})
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
        if student_object.save:
            print("successfully registerd")
        return render(request, 'registration.html', {"success": "successfully registerd "})
    return render(request, 'registration.html')


def markslist(request):
    return render(request, 'markslist.html')


def marksview(request):
    userid = request.session["user"]
    student_marks = addmarks.objects.filter(id_no=userid)
    return render(request, 'marksview.html', {"studentsinfo": student_marks})



def StuMarks(request):
    print(request)
    if request.method == "POST":
        print("its a post method")
        student_object = addmarks.objects.create()
        student_object.id_no = request.session['user']
        student_object.maths = request.POST["maths"]
        student_object.physics = request.POST["physics"]
        student_object.chemistry = request.POST["chemistry"]
        print("student_object before")
        student_object.save()
        print("student_object after")

    return render(request, 'addmarks.html')


def Users(request):
    student_list = studentinfo.objects.all()
    print(student_list)
    return render(request, 'alluser.html')

def home(request):
    print(request)
    return render(request, 'home.html')

def index(request):
    print(request)
    return render(request, 'index.html')


def details(request):
    print(request)
    userid = request.session["user"]
    student_details = studentinfo.objects.filter(id=userid)
    return render(request, 'mydetails.html', {"studentsinfo": student_details})

