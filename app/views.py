from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class HomePageView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        return render(request, "index.html")
