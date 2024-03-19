from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_message_length(value):
    if len(value) < 10:
        raise ValidationError(_('A mensagem deve ter pelo menos 10 caracteres.'), code='invalid_length')

