from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import UserRegisterForm
import requests

class HomePageVew(View):
    def get(self, request):
        return render(request, 'home.html')

class RegisterPageView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            url = 'http://localhost:8001/auth/register'
            data = {
                "username": username,
                "email": email,
                "password": password
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                return HttpResponse("User registered successfully!")
            else:
                return HttpResponse(f"Error: {response.json()['detail']}")
        else:
            form = UserRegisterForm()
            return render(request, 'register.html', {'form': form})
