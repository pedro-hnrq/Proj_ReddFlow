from django.urls import path
from . import views

urlpatterns = [
    # Páginas de Cadastrar usuários - /auth/register
    path('register/', views.register, name="register"),
    # Páginas de Login - /auth/login/
    path('login/', views.login, name="login"),
     # Sai - /auth/logout
    path('logout/', views.logout_user, name="logout"),
    # Conta - /account/
    path('account/', views.account, name='account'),
]
