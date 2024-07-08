from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
from .validators import validate_message_length
from .choices import CATEGORY_CHOICES

class Topic(models.Model):
    subject = models.CharField(_('Assunto'), max_length=100, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Autor(a)'), on_delete=models.CASCADE)
    category = models.CharField(_('Categoria'), max_length=100, choices=CATEGORY_CHOICES)
    image = models.ImageField(_('Imagem'), upload_to='imagem_forum/', blank=True, null=True)
    message = models.TextField(_('Mensagem'))
    date_posted = models.DateTimeField(_('Data de Postagem'), auto_now_add=True)
    date_modified = models.DateTimeField(_('Data de Modificação'), auto_now=True)

    class Meta:
        db_table = "posts"
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"

    def __str__(self):
        return self.subject

class Comment(models.Model):
    topic = models.ForeignKey(Topic, verbose_name=_('Tópico'), on_delete=models.CASCADE)
    Commentator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Comentarista'), on_delete=models.CASCADE)
    message = models.TextField(_('Mensagem'), validators=[validate_message_length])
    date_posted = models.DateTimeField(_('Data de Postagem'), auto_now_add=True)
    date_modified = models.DateTimeField(_('Data de Modificação'), auto_now=True)

    class Meta:
        db_table = "comments"
        verbose_name = _("Comentário")
        verbose_name_plural = _("Comentários")

    def __str__(self):
        return f'Comentário no {self.topic.subject}'
