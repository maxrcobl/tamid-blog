from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = {
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', views.PostListView.as_view(), name='post-list'),
}