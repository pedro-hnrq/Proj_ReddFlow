from django import forms
from .models import Topic, Comment
from .validators import validate_message_length 
from django.core.exceptions import ValidationError


class TopicForm(forms.ModelForm):
    message = forms.CharField(validators=[validate_message_length])  

    class Meta:
        model = Topic
        fields = ['subject', 'category', 'image', 'message']
        
    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if Topic.objects.filter(subject__iexact=subject).exists():
            raise ValidationError("Já existe um tópico com este assunto.")
        return subject

class CommentForm(forms.ModelForm):
    message = forms.CharField(validators=[validate_message_length]) 

    class Meta:
        model = Comment
        fields = ['message']