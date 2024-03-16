# Generated by Django 5.0.3 on 2024-03-16 23:01

import account.models
import account.validators
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('first_name', models.CharField(max_length=50, validators=[account.validators.validate_name_characters], verbose_name='Nome')),
                ('last_name', models.CharField(max_length=50, validators=[account.validators.validate_name_characters], verbose_name='Sobrenome')),
                ('date_birth', models.DateField(validators=[account.validators.validate_age_18_or_above], verbose_name='Data de Nascimento')),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1, verbose_name='Sexo')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('change_date', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Membro da equipe')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
            managers=[
                ('objects', account.models.AccountManager()),
            ],
        ),
    ]
