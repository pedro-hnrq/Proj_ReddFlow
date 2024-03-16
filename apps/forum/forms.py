from django import forms
from .models import Topic, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'category', 'image', 'message']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']