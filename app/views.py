from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import View


# Create your views here.
class HomePageView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        return render(request, "index.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_revalidation = request.POST.get("password_revalidation")
        email = request.POST.get("email")
        if password != password_revalidation:
            messages.error(request, "Your passwords didn't match, please try again.")
            context = {"username": username, "email": email, "password": password}
            return render(request, "register.html", context)
        else:
            new_user = User.objects.create_user(
                username=username, email=email, password=password
            )

            print(new_user)
            return redirect("login")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember")
        next_url = request.POST.get("next", request.GET.get("next", "home"))

        authenticate_user = authenticate(request, username=username, password=password)

        if authenticate_user is None:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("login")
        else:
            login(request, authenticate_user)

            # Set session expiry based on remember me checkbox
            if not remember_me:
                # Session expires when browser closes
                request.session.set_expiry(0)
            else:
                # Session expires after 2 weeks (in seconds)
                request.session.set_expiry(1209600)

            return redirect(next_url)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")
