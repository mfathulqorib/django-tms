import os
from urllib import request

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import DetailView, View
from apps.users.models import ProfileUser

from .forms import ProfileForm, UserForm


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")

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


class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_revalidation = request.POST.get("password_revalidation")
        email = request.POST.get("email")

        register_input = {"username": username, "email": email, "password": password}

        if password != password_revalidation:
            messages.error(request, "Your passwords didn't match, please try again.")
            return render(request, "users/register.html", register_input)

        existing_user = User.objects.filter(
            Q(username__iexact=username) | Q(email__iexact=email)
        ).first()

        if existing_user:
            if existing_user.username.lower() == username.lower():
                messages.error(
                    request, "Username already taken, please choose another one."
                )
            else:
                messages.error(
                    request, "Email already registered. Please choose another one."
                )

            return render(request, "users/register.html", register_input)

        new_user = User(username=username, email=email, is_active=False)
        new_user.set_password(password)
        new_user.save()

        try:
            self._send_activation_email(request, new_user)
            return redirect("login")
        except Exception as e:
            new_user.delete()
            messages.error(request, f"Failed to send confirmation email: {e}")
            return render(request, "users/register.html", register_input)

    def _send_activation_email(self, request, new_user):
        # Send confirmation email
        current_site = get_current_site(request)
        uid = urlsafe_base64_encode(force_bytes(new_user.pk))
        token = default_token_generator.make_token(new_user)
        confirm_link = reverse("activate", kwargs={"uidb64": uid, "token": token})
        protocol = "https" if request.is_secure() else "http"
        activation_url = f"{protocol}://{current_site.domain}{confirm_link}"

        subject = "Activate your account."
        message = render_to_string(
            "users/activation_email.html", {"activation_url": activation_url}
        )
        try:
            send_mail(
                subject,
                message,
                os.getenv("EMAIL_HOST_USER"),
                [new_user.email],
                fail_silently=False,
                html_message=message,
            )
            messages.success(
                request, "Please check your email to activate your account."
            )
        except Exception as e:
            messages.error(request, f"Failed to send confirmation email: {e}")


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


class ProfileDetailView(DetailView):
    template_name = "users/profile.html"
    context_object_name = "profile"

    def get_object(self):
        return getattr(self.request.user, "profile", None)


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        profile_form = ProfileForm(instance=request.user.profile)
        user_form = UserForm(instance=request.user)

        return render(
            request,
            "users/profile_edit.html",
            {"profile_form": profile_form, "user_form": user_form},
        )

    def post(self, request):
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your account has been updated.")
            return redirect("profile")
        else:
            messages.error(request, "An error occurred. Please check your inputs.")
            return render(
                request,
                "users/profile_edit.html",
                {"profile_form": profile_form, "user_user": user_form},
            )

# class ProfileUpdateView(LoginRequiredMixin, View):
#     login_url = "/login"
#
#     def get(self, request):
#         user = self.request.user
#         profile = ProfileUser.objects.get(user=user)
#
#         context = {"user": user, "profile": profile}
#         return render(request, "users/profile_edit.html", context)
