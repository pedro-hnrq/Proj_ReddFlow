from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
from .validators import validate_message_length
from .choices import CATEGORY_CHOICES

class Topic(models.Model):
    subject = models.CharField(_('Assunto'), max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Autor(a)'), on_delete=models.CASCADE)
    category = models.CharField(_('Categoria'), max_length=100, choices=CATEGORY_CHOICES)
    date_posted = models.DateTimeField(_('Data de Postagem'), auto_now_add=True)
    image = models.ImageField(_('Imagem'), upload_to='imagem_forum/', blank=True, null=True)
    message = models.TextField(_('Mensagem'))

    class Meta:
        verbose_name = "Tópico"
        verbose_name_plural = "Tópicos"

    def __str__(self):
        return self.subject

class Comment(models.Model):
    topic = models.ForeignKey(Topic, verbose_name=_('Tópico'), on_delete=models.CASCADE)
    Commentator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Comentarista'), on_delete=models.CASCADE)
    date_posted = models.DateTimeField(_('Data de Postagem'), auto_now_add=True)
    message = models.TextField(_('Mensagem'), validators=[validate_message_length])

    class Meta:
        verbose_name = _("Comentário")
        verbose_name_plural = _("Comentários")

    def __str__(self):
        return f'Comentário no {self.topic.subject}'
