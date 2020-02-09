from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.contrib import messages

# Create your views here.
def user_login_required(f):
    def wrap(request, *args, **kwargs):
        # this check the session if userid key exist, if not it will redirect
        # to login page
        if 'user' not in request.session.keys():
            return HttpResponseRedirect("/student/login")
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


def login(request):
    if request.method == 'POST':
        print("post method calling")
        email = request.POST['email']
        password = request.POST['pwd']
        student_object = studentinfo.objects.filter(email=email, password=password)
        if student_object:
            print("email and password")
            request.session["user"] = student_object[0].id
            # return render(request, 'home.html', {"studentinfo": student_object[0]})
            return HttpResponseRedirect("/student/home/")

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

@user_login_required
def marksview(request):
    userid = request.session["user"]
    student_marks = addmarks.objects.filter(id_no=userid)
    return render(request, 'marksview.html', {"studentsinfo": student_marks})



@user_login_required
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
    print(request)
    student_list = studentinfo.objects.all()
    print(student_list)
    return render(request, 'alluser.html', {'studentinfo': student_list})


@user_login_required
def home(request):
    print(request)
    student_object = studentinfo.objects.filter(id=request.session["user"])
    print(student_object)
    return render(request, 'home.html', {"studentinfo": student_object[0]})
    # return render(request, 'home.html')


def index(request):
    print(request)
    return render(request, 'index.html')

@user_login_required
def details(request):
    print(request)
    userid = request.session["user"]
    student_details = studentinfo.objects.filter(id=userid)
    return render(request, 'my_details.html', {"studentsinfo": student_details})


def password(request):
    print(request)
    if request.method == 'POST':
        print("post method calling")
        email = request.POST['email']
        student_pass = studentinfo.objects.filter(email=email)
        if student_pass:
            print("email")
            return render(request, 'forgot_password.html', {"studentinfo": f'Password sent to {email}'})
        else:
            print("invalid email ")
            return render(request, 'forgot_password.html', {"error": "invalid email"})

    return render(request, 'forgot_password.html')


def logout(request):
    print(request, "logout calling")
    del request.session["user"]
    return HttpResponseRedirect("/student/login/")


def fees(request):
    print(request)
    if request.method == 'POST':
        print("it's post methed")
        stufee_object = fee.objects.create()
        stufee_object.first = request.POST["first"]
        stufee_object.second = request.POST["second"]
        stufee_object.third = request.POST["third"]
        stufee_object.fourth = request.POST["fourth"]
        stufee_object.fifth = request.POST["fifth"]
        stufee_object.sixth = request.POST["sixth"]
        stufee_object.seventh = request.POST["seventh"]
        print("stufee_object before")
        stufee_object.save()
        print("stufee_object after")

    return render(request, "fee.html")


def presentfees(request):
    print(request)
    present_fee = fee.objects.all()
    print(present_fee)
    return render(request, 'presentfee.html', {"fee": present_fee})


def depart(request):
    print(request)
    return render(request, 'departments.html')
