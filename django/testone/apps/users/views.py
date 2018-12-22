from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, handlers
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile
from .forms import LoginForm, RegisterForm
from utils.email_send import send_register_email
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as er:
            return None

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {"login_form": login_form, "loginer": "登陆失败！用户名或密码错误！"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register = RegisterForm()
        return render(request, 'register.html', {"register": register})
    def post(self, request):
        register = RegisterForm(request.POST)
        if register.is_valid():
            username = request.POST.get('email', '')
            password = request.POST.get('password', '')
            registeruser = UserProfile()
            registeruser.username = username
            registeruser.email = username
            registeruser.password = make_password(password)
            # registeruser.save()
            send_register_email(username, "register")
            return render(request,'login.html', {})
        else:
            return render(request, 'register.html', {"register": register})