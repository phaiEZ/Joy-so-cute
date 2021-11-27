from django.contrib.messages.api import MessageFailure
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, "backend/login_register.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if username == "" or email == "" or password == "" or repassword == "":
            messages.info(request, "*กรุณสป้อนข้อมูลให้ครบให้ครบ")
            return redirect('member')
        else:
            if password == repassword:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                messages.info(request, "*create complete")

            else:
                messages.info(request, "*password not match")
            return redirect('member')
