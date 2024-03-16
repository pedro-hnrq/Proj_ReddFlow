import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta

def validate_age_18_or_above(value):
    """
    Valida se a data de nascimento é igual ou superior a 18 anos.
    """
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError(_('Você deve ter pelo menos 18 anos para se cadastrar.'), code='invalid_age')

def validate_name_characters(value):
    """
    Valida se o campo contém apenas letras.
    """
    if not re.match("^[a-zA-Z]*$", value):
        raise ValidationError(_('Este campo deve conter apenas letras.'), code='invalid_characters')
