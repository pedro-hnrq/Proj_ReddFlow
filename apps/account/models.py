from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


from .validators import  validate_age_18_or_above, validate_name_characters

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
   
        
        return self._create_user(email, password, **extra_fields)

class CustomAuthor(AbstractUser):
    SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    ]

    email = models.EmailField(_('E-mail'), unique=True)
    first_name = models.CharField(_('Nome'), max_length=50, validators=[validate_name_characters])
    last_name = models.CharField(_('Sobrenome'), max_length=50, validators=[validate_name_characters])
    date_birth = models.DateField(_('Data de Nascimento'), validators=[validate_age_18_or_above], blank=True, null=True)
    sex = models.CharField(_('Sexo'), max_length=1, choices=SEX_CHOICES, blank=True)
    creation_date = models.DateTimeField(_('Data de Criação'), auto_now_add=True) 
    change_date = models.DateTimeField(_('Data de Alteração'), auto_now=True)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta():
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")
    
    def __str__(self):
        return self.email
    
    objects = AccountManager()
