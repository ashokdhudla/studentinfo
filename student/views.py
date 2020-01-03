from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request,'login.html')


def registration(request):
    print(request)
    if request.method == "POST":
        print("it's a POST method")
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        birthday = request.POST["Birthday"]
        gender = request.POST["gender"]
        submit = request.POST["submit"]
        reset = request.POST["reset"]
        print(firstname, lastname, email, password, birthday, gender, submit, reset)

    return render(request,'registration.html')

