from django.contrib import admin
from .models import CustomAuthor
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm


@admin.register(CustomAuthor)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomAuthor
    list_display = ("email", "first_name", "last_name", "is_staff")
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'date_birth', 'sex')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('creation_date', 'change_date')}),
    )    
    readonly_fields = ('creation_date', 'change_date')
    search_fields = ('first_name', 'last_name')
    