from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,template_name="index.html")


def login_view(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            messages.info(request, "username or password is incorrect")
    else:
         return render(request, template_name="pages/login.html")

    return render(request, template_name="pages/login.html")


@login_required(login_url="login-view")
def dashboard(request):
    return render(request, template_name="pages/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login-view")