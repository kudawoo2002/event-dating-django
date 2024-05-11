from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms 
# Create your views here.

def home(request):
    return render(request,template_name="index.html")

@login_required(login_url="login-view")
def dating(request):
    return render(request, template_name="pages/dating.html")


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


def register(request):
    form = CreateUserForms()
    context ={'form': form}
    if request.method == "POST":
        form = CreateUserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login-view")
        else:
            messages.info(request, "invalid field or password does not the requirement")
            return render(request,template_name="pages/register.html", context=context)
        
    
    return render(request,template_name="pages/register.html", context=context)

@login_required(login_url="login-view")
def dashboard(request):
    return render(request, template_name="pages/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login-view")