from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import Profile
from django.conf import settings
from django.urls import reverse
import uuid

class ForumPost(models.Model):
    """docstring for Post."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    post_text = models.TextField()
    forum_post = models.ForeignKey('self', null=True, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object"""
        return self.ForumPost

    def get_absolute_url(self):
        """Returns the url to access a detail record for the post"""
        return reverse('forum:post_detail', args=[str(self.id)])

class Comment(models.Model):
    """docstring for Comment."""
    forumpost = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000)
    replied_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['replied_at']

    def __str__(self):
        """String for representing the Model object"""
        return self.Comment

    def get_absolute_url(self):
        """Returns the url to access a detail record for the post"""
        return reverse('forum:post_detail', args=[str(self.id)])
