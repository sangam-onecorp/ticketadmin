import re
from django.shortcuts import render,redirect
from datetime import datetime
from .queries import *
# Create your views here.
def dashboard(request):
    print("dashboard")
    return render(request,'dashboard.html')

# Create your views here.
def Signup(request):
    print("Signup")
    contextmsg={}
    if request.method == "POST":
        print("Print I am post request ",request.POST['fName'])
        print("Print I am post request ",request.POST['lName'])
        print("Print I am post request ",request.POST['pass'])
        print("Print I am post request ",request.POST['pass2'])
        print("Print I am post request ",request.POST['location'])
        print("Print I am post request ",request.POST['phone'])
        print("Print I am post request ",request.POST['email'])
        data={
        "UserName" : request.POST['fName']+request.POST['lName'],
        "FirstName" : request.POST['fName'],
        "LastName" : request.POST['lName'],
        "Phone" : request.POST['phone'],
        "Password" : request.POST['pass'],
        "Email" : request.POST['email'],
        "AccessLevel" : "User",
        "Location" : request.POST['location'],
        "IsDeleted" : 0,
        "CreatedAt" : datetime.now(),
        "CreatedBy" : "System",
        "UpdatedAt" : datetime.now(),
        "UpdatedBy" : "System" }
        if request.POST['pass'] != request.POST['pass2']:
            contextmsg={"Error":"Password should matched."}
        else:
            UserSignup_q(data.values())
            return redirect(Login)
    return render(request,'signup.html',contextmsg)


# Create your views here.
def Login(request):
    print("Login")
    return render(request,'login.html')