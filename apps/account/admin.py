from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomAuthorCreateForm, CustomAuthorChangeForm
from .models import CustomAuthor

@admin.register(CustomAuthor)
class CustomAuthorAdmin(UserAdmin):
    add_form = CustomAuthorCreateForm
    form = CustomAuthorChangeForm
    model = CustomAuthor
    list_display = ('email', 'first_name', 'last_name', 'date_birth', 'sex', 'is_staff')  
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
