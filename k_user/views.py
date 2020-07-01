from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def main_page(request):
    return render(request, 'k_user/main_page.html', {})


def signup_page(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('main_page')
        return render(request, "k_user/signup_page.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("main_page")
        else:
            return render(request, "k_user/login_page.html", {'error': 'username or password is incorrect'})

    else:
        return render(request, "k_user/login_page.html")


def logout_page(request):
    auth.logout(request)
    return redirect("main_page")