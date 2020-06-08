from django.db import models
from django.forms import ModelForm
from forum.models import ForumPost, Comment

class PostForm(ModelForm):
    class Meta:
        model = ForumPost
        fields = ('title', 'post_text',)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
