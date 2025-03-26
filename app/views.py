from decouple import config
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
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
                username=username, email=email, password=password, is_active=False
            )

            print(new_user)

            # Send confirmation email
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(new_user.pk))
            token = default_token_generator.make_token(new_user)
            confirm_link = reverse("activate", kwargs={"uidb64": uid, "token": token})
            activation_url = f"http://{current_site.domain}{confirm_link}"

            subject = "Activate your account."
            message = render_to_string(
                "activation_email.html", {"activation_url": activation_url}
            )
            try:
                send_mail(
                    subject,
                    message,
                    config("EMAIL_HOST_USER"),
                    [email],
                    fail_silently=False,
                    html_message=message,
                )
                messages.success(
                    request, "Please check your email to activate your account."
                )
            except Exception as e:
                messages.error(request, f"Failed to send confirmation email: {e}")

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


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                request, "Your account has been activated. You can now log in."
            )
            return redirect("login")
        else:
            messages.error(request, "Invalid activation link.")
            return redirect("login")
