from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model, login as login_auth, authenticate, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import RegisterForm, AuthForm, UpdateForm
from .decorators import not_authenticated
from forum.views import topic_view

@not_authenticated
def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = True
            user.save()
            messages.success(request, 'Conta criada com sucesso. Faça login para continuar.')
            return redirect(reverse('login'))
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

@not_authenticated
def login(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            email = auth_form.cleaned_data.get('email')
            password = auth_form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login_auth(request, user)
                return redirect('/')
        messages.add_message(request, constants.ERROR, "E-mail ou senha incorretos.")
    else:
        auth_form = AuthForm()
    return render(request, 'login.html', {'auth_form': auth_form})

def user_logout(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, "Você foi deslogrado.")
    return redirect(reverse('login'))

@login_required
def user_login(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            email = auth_form.cleaned_data.get('email')
            password = auth_form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login_auth(request, user)
                return redirect('forum:topic_view')
        messages.add_message(request, constants.ERROR, "E-mail ou senha incorretos.")
    else:
        auth_form = AuthForm()
    return render(request, 'accounts/login.html', {'auth_form': auth_form})


def logout_user(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, "Você foi deslogrado.")
    return redirect(reverse('login'))

@login_required
def account(request):
    if request.method == 'POST':
        user_form = UpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Informações da conta atualizadas com sucesso!')
            return redirect('topic_view')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        user_form = UpdateForm(instance=request.user)
    return render(request, 'account.html', {'user_form': user_form})