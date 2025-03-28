from django.urls import path

from app.views import (ActivateAccountView, HomePageView, LoginView,
                       LogoutView, RegisterView)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
]
