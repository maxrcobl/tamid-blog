from django.urls import path, include
from . import views

urlpatterns = [
    # Home page for the app - displays posts in a list
    path('', views.PostListView.as_view(), name='post-list'),
    # Path to the detialed view of the posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # Page for creating new posts
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    # Page for updating posts
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    # Page for deleting posts
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    # Page for registering a new user or signing in
    path('register/', views.RegisterView.as_view(), name='register')
]
