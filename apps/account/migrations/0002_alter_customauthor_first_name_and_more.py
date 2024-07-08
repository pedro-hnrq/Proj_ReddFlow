# Generated by Django 5.0.3 on 2024-07-08 14:25

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customauthor',
            name='first_name',
            field=models.CharField(db_index=True, max_length=50, validators=[account.validators.validate_name_characters], verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='customauthor',
            name='last_name',
            field=models.CharField(db_index=True, max_length=50, validators=[account.validators.validate_name_characters], verbose_name='Sobrenome'),
        ),
        migrations.AlterModelTable(
            name='customauthor',
            table='authors',
        ),
    ]