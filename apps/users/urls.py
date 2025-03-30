from django.urls import path

from .views import LoginView, LogoutView, ActivateAccountView, RegisterView, ProfileDetailView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileDetailView.as_view(), name="profile"),
]