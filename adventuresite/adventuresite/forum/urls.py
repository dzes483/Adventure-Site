from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'forum'

urlpatterns = [
    path('posts/', views.ForumPostListView.as_view(), name='post_list'),
    path('new_post/', views.ForumPostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/delete/', views.ForumPostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/delete', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('post/comment/<int:pk>/delete', views.CommentDetailView.as_view(), name='comment_detail')
]
