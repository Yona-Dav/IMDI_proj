from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('homepage')


def logout_view(request):
    logout(request)
    return redirect('homepage')


class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile.html'





