from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from .validators import validate_age_18_or_above
from .models import CustomAuthor

class CustomAuthorCreateForm (UserCreationForm):
     
     class Meta:
          model = CustomAuthor
          fields = ['first_name', 'last_name',]
          labels = {'email': 'E-mail'}
          
     def save(self, commit=True):
          user = super().save(commit=False)
          user.set_password(self.cleaned_data["password1"])
          user.email = self.cleaned_data["email"]
          if commit:
               user.save()
          return user
     
class CustomAuthorChangeForm(UserChangeForm):
     
     class Meta:
          model = CustomAuthor
          fields = ['first_name', 'last_name', 'date_birth', 'sex', 'email']


class RegisterForm(CustomAuthorCreateForm):
    '''Formulário para cadastro de usuários sem permissões 
    administrativas apartir do Email, first_name, last_name, date_birth, sex e senha'''

    date_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomAuthor
        fields = ('first_name', 'last_name', 'email', 'date_birth', 'sex', 'password1', 'password2')
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'date_birth': 'Data de Nascimento',
            'sex': 'Sexo',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'sex': forms.Select(choices=CustomAuthor.SEX_CHOICES, attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['date_birth'].widget.attrs.update({'class': 'form-control'})
        for field in self.fields:
            if 'password' in field:
                self.fields[field].help_text = None
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
    def clean_date_birth(self):
        date_birth = self.cleaned_data['date_birth']
        validate_age_18_or_above(date_birth)
        return date_birth

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomAuthor.objects.filter(email=email).exists():
            raise forms.ValidationError("Este endereço de email já existe.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não correspondem")
        return cleaned_data

class AuthForm(forms.Form):
    email = forms.EmailField(
        label = "Email",
        max_length = 254,
        widget= forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
            label = "Senha",
            strip = False,
            widget = forms.PasswordInput(attrs={'class': 'form-control'})
    )

    error_messages = {
        'invalid_login': 'E-mail ou senha inválidos',
        'inactive': 'E-mail inátivo',
    }

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        self.user = authenticate(username=email, password=password)

        if not self.user:
            raise self.get_invalid_login_error()
        else:
            self.confirm_user_active()
        return self.cleaned_data

    def log_into(self, request):
        if not self.user:
            raise TypeError('self.user não pode ser None, execute form.is_valid() primeiro')

        login(request, self.user)
        return self.user

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
        )

    # Verificar se usuário está Ativo

    def confirm_user_active(self):
        if not self.user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )