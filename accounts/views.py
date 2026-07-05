from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_user(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah digunakan!")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registrasi berhasil! Silakan login.")
        return redirect("login")

    return render(request, "register.html")


def login_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Selamat datang, {username}!")
            return redirect("/")
        else:
            messages.error(request, "Username atau Password salah!")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Berhasil Logout.")
    return redirect("/")