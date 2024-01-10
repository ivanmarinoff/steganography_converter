from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from .forms import UserSignUpForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout


class RegisterView(View):
    template_name = "../templates/users/signup.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("welcome-page")
        form = UserSignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Print message
            UserName = form.cleaned_data.get('username')
            messages.success(request, f'{UserName}: Account Created!')
            return redirect('login')
        # else:
        else:
            form = UserSignUpForm()
        return render(request, '../templates/users/signup.html', {'form': form})


class LoginView(View):
    template_name = "../templates/users/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("welcome-page")
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("welcome-page")
        else:
            return render(request, self.template_name, {'form': UserLoginForm()})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")
