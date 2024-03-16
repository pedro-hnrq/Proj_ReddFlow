from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_message_length(value):
    if len(value) < 10:
        raise ValidationError(_('A mensagem deve ter pelo menos 10 caracteres.'), code='invalid_length')

# def validate_category(value):
#     """
#     Valida a categoria do tópico.
#     Aqui você pode adicionar suas próprias regras de validação, se necessário.
#     """
#     # Exemplo: Verifica se a categoria está em uma lista de categorias válidas
#     valid_categories = ['Tecnologia', 'Esportes', 'Entretenimento', 'Política']
#     if value not in valid_categories:
#         raise ValidationError(_('Categoria inválida.'), code='invalid_category')
