from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from forum.models import ForumPost, Comment
from forum.forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import forms
from django.urls import reverse, reverse_lazy

class ForumPostCreateView(LoginRequiredMixin, CreateView):
    """docstring for ForumPostCreateView."""
    model = ForumPost
    fields = ('title', 'post_text')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

def post_detail(request, pk):
    template_name = 'forum/forumpost_detail.html'
    forumpost = get_object_or_404(ForumPost, pk=pk)
    user = request.user
    comments = forumpost.comments.filter(active=True)
    request.session['num_comments'] = forumpost.comments.all().count()
    num_comments = request.session['num_comments']
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.user = user
            # Assign the current post to the comment
            new_comment.forumpost = forumpost
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'forumpost': forumpost,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'num_comments': num_comments,})

class ForumPostListView(ListView):
    model = ForumPost
    template_name = 'forumpost_list.html'
    paginate_by = 10
    ordering = ['-created_at']

    def comments(request):
        num_comments = request.session['num_comments']
        return render (request, template_name, {'num_comments': num_comments,})

class ForumPostDeleteView(LoginRequiredMixin, DeleteView):
    model = ForumPost
    success_url = reverse_lazy('forum:post_list')


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('forum:post_list')

class CommentDetailView(LoginRequiredMixin, DetailView):
    """docstring for CommentDetailView."""

    model = Comment
    template_name = 'forum/comment_detail.html'
