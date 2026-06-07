from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create tag model
class Tag(models.Model):
    # Only field is the name, limited to 50 characters, and preventing duplicates
    name = models.CharField(max_length=50, unique=True)

    # Displays the name of the tag when selecting tags
    def __str__(self):
        return self.name

# Create post model and define the fields
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # .ForeignKey links each post to one user; deleting a user deletes their posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    # .ManyToManyField allows a post to have unlimited tags and a tag to be linked to unlimited posts
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True)

    def __str__(self):
        return self.title