from datetime import datetime
import re
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


def login(request):
    if request.method=="POST":
        try:
            usernameInput = request.POST["username"]
            passwordInput = request.POST["password"]

            if request.POST.get("Register"):
                result=register(request)
                if result=="success":
                    return render(request,"index.html",{"usercreated_message":"User registered succesfully"})

            if usernameInput == "" or passwordInput == "":
                return HttpResponse({"GetToken": "invalid"})

            # user = authenticate(username=usernameInput, password=passwordInput)
            # user=User.objects.filter(username=usernameInput,password=passwordInput).get()
            user=authenticate(username=usernameInput,password=passwordInput)

            if not user:
                return render(request,"index.html")
            # token = Token.objects.get_or_create(user=user)

            # request.session["tokenValue"]=token

            request.session['username']=usernameInput

            # return render(request,"home-view.html")
            return redirect("home-view")
        except:
            return render(request,"index.html")
    
    return render(request,"index.html")


def register(request):
    usernameInput = request.POST["username"]
    passwordInput = request.POST["password"]

    # user=authenticate(username=username,password=password)
 
    new_user = User.objects.create_user(
        username=usernameInput, password=passwordInput,last_login=datetime.now())
    
    # token,_ = Token.objects.get_or_create(user=new_user)
    return "success"
    # return render(request,"index.html",{"usercreated_message":"User registered succesfully"})

def logout(request):
    if request.session.has_key('username'):
        request.session.flush()
        return redirect('http://127.0.0.1:8000/')
    else:
        return redirect('http://127.0.0.1:8000/')