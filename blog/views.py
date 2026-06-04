from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Post.objects.filter(is_public=True) | Post.objects.filter(author=self.request.user)
        else:
            queryset = Post.objects.filter(is_public=True)
        
        
        query = self.request.GET.get('q')
        tag = self.request.GET.get('tag')
        author = self.request.GET.get('author')

        if query:
            queryset = queryset.filter(title__icontains=query)
        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)
        if author:
            queryset = queryset.filter(author__username__icontains=author)
        
        return queryset.distinct()
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'is_public', 'tags', 'image']
    success_url = reverse_lazy('post-list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'is_public', 'tags', 'image']
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class RegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    scucess_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

