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
    student_list = studentinfo.objects.all()
    print(student_list)
    return render(request, 'alluser.html')


@user_login_required
def home(request):
    print(request)
    student_object=studentinfo.objects.filter(id=request.session["user"])
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
    student_object = studentinfo.objects.filter(id=userid)
    return render(request, 'my_details.html', {"studentsinfo": student_object})


def password(request):
    print(request)
    if request.method == 'POST':
        print("post method calling")
        email = request.POST['email']
        student_pass = studentinfo.objects.filter(email=email)
        if student_pass:
            print("email")
            return render(request, 'forgot_password.html', {"studentinfo": f'Password sent to {email}'} )
        else:
            print("invalid email ")
            return render(request, 'forgot_password.html', {"error": "invalid email"})

    return render(request, 'forgot_password.html')

def logout(request):
    print(request,"logout calling")
    del request.session["user"]
    return HttpResponseRedirect("/student/login/")


def staff_names(request):
    print(request)
    if request.method == "GET":
        subjects=Subject.objects.all()
        return render(request, 'staff.html',{"subjects":subjects})
    if request.method == "POST":
        print("its a post method")
        staff_object = staff.objects.create()
        staff_object.firstname = request.POST["firstname"]
        staff_object.lastname = request.POST["lastname"]
        staff_object.email = request.POST["email"]
        print("requst.post",request.POST["subject"])
        staff_object.subject = Subject.objects.get(id_no=int(request.POST["subject"]))

        print("staff_object before")
        staff_object.save()
        print("staff_object after")

    return render(request, 'staff.html')

def sub_name(request):
    print(request)
    if request.method == "POST":
        print("its a post method")
        sub_object = Subject.objects.create()

        sub_object.subjectname = request.POST["subjectname"]
        print("sub_object before")
        sub_object.save()
        print("sub_object after")

    return render(request, 'subject.html')


def staffdetails(request):
    print(request)
    staff_details = staff.objects.all()
    print(staff_details)
    return render(request, 'staffdetails.html', {"staffdetails": staff_details})


def admin (request):
    return render(request, 'admin.html')





