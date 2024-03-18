from django.contrib import admin
from .models import CustomAuthor
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm


@admin.register(CustomAuthor)
class UserAdmin(admin_auth_django.UserAdmin):
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

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # Se estiver editando um objeto existente
            readonly_fields += ('email', 'creation_date', 'change_date')
        return readonly_fields
    