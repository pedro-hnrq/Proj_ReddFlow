from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomAuthor

class CustomAuthorCreateForm (UserCreationForm):
     
     class Meta:
          model = CustomAuthor
          fields = ['first_name', 'last_name',]
          labels = {'username': 'E-mail'}
          
     def save(self, commit=True):
          user = super().save(commit=False)
          user.set_password(self.cleaned_data["password1"])
          user.email = self.cleaned_data["username"]
          if commit:
               user.save()
          return user
     
class CustomAuthorChangeForm(UserChangeForm):
     
     class Meta:
          model = CustomAuthor
          fields = ['first_name', 'last_name', 'date_birth', 'sex', 'email']
