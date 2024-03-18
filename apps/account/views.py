from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model, login as login_auth, authenticate, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm, AuthForm
from .decorators import not_authenticated
from forum.views import topic_view

@not_authenticated
def register(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        if request.user.is_authenticated:
                  HttpResponse('Erro: Usuário já está autenticado.')
         #    return redirect('forum:')
        return render(request, 'register.html', {'register_form': register_form})
    elif request.method == "POST": 
        register_form = RegisterForm(request.POST) 
        
        if register_form.is_valid(): 
                  form_new = register_form.save(commit=False)
                  form_new.is_active = False           
                  form_new.save() 
                  return redirect(reverse('login'))
        else: 
                  return render(request, 'register.html', {'register_form': register_form})

def active_account(request, uidb4, token):
         
         User = get_user_model()
         uid = force_str(urlsafe_base64_decode(uidb4))
         user = User.objects.filter(pk=uid)
         print(user)
         if (user := user.first()) and default_token_generator.check_token(user, token):
                  user.is_active = True
                  user.save()
                  login_auth(request, user)
                  messages.add_message(request, constants.SUCCESS, "Seu usuário foi ativado com sucesso.")
                  return redirect(reverse('login'))
         else:
                  messages.add_message(request, constants.ERROR, "A URL acessada não é válida.")
                  return redirect(reverse('login'))

@not_authenticated
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('')
        auth_form = AuthForm()
        return render(request, 'login.html', {'auth_form': auth_form})
    elif request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            email = auth_form.cleaned_data.get('email')
            password = auth_form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login_auth(request, user)
                return redirect('forum:topic_view')
        messages.add_message(request, constants.ERROR, "E-mail ou senha incorretos.")
        return redirect(reverse('login'))

def logout_user(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, "Você foi deslogado.")
    return redirect(reverse('login'))
