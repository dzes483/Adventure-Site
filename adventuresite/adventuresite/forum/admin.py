from django.contrib import admin
from .models import ForumPost, Comment
# Register your models here.
admin.site.register(ForumPost)
admin.site.register(Comment)
