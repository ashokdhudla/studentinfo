from django.shortcuts import render

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
        FirstName=request.POST["FirstName"]
        LastName= request.POST["LastName"]
        EmailAddress=request.POST["email"]
        Birthday=request.POST["Birthday"]
        Gender=request.POST["Gender"]
        print(FirstName,LastName,EmailAddress,Birthday,Gender)
    return render(request,'registration.html')

def markslist(request):
    return render(request,'markslist.html')

def marksview(request):
    return render(request,'marksview.html')
