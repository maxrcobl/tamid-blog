from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

# Create your views here.

# Inherits the ListView class from Django: All views inherit a "template" view defined by Django
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    # Defines the function for sorting posts by criteria
    def get_queryset(self):
        # If user is logged in. If yes -> show their own posts OR public posts. If no -> Show public posts
        if self.request.user.is_authenticated:
            queryset = Post.objects.filter(is_public=True) | Post.objects.filter(author=self.request.user)
        else:
            queryset = Post.objects.filter(is_public=True)
        
        
        query = self.request.GET.get('q')
        tag = self.request.GET.get('tag')
        author = self.request.GET.get('author')
        
        # Three fields to filter by: tag, author, and title (query)
        if query:
            queryset = queryset.filter(title__icontains=query)
        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)
        if author:
            queryset = queryset.filter(author__username__icontains=author)
        
        # Return the queryset, filter out duplicates
        return queryset.distinct()
    
# Inherits the DetailView class from Django
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# LoginRequiredMixin requires that the user is logged in. If not, redirects to the login page
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    # the fields for creating a post
    fields = ['title', 'content', 'is_public', 'tags', 'image']
    # When post is created, reverse searches for the "post-list" url and returns that url
    success_url = reverse_lazy('post-list')
    
    # Ensures the fields in the post creation have valid entries
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'is_public', 'tags', 'image']
    success_url = reverse_lazy('post-list')

    # Decides if current user is allowed to acces PostUpdateView
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    # Same function as PostUpdateView
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# View for registering a user
class RegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post-list')

    # Checks entires are valid (username, password)
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

