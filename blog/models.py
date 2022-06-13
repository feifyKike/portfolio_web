from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    """Showing a particular category"""
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Displaying a string representation"""
        return self.name

class Post(models.Model):
    """Creating category related posts"""
    title = models.CharField(max_length=200)
    snippet = models.TextField(max_length=255, default="Follow the link above to the blog post.")
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        """Showing a shortened string representation"""
        return self.title

class Comment(models.Model):
    """Add comments to answer posts"""
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        """Showing a part of the comment"""
        return self.author + ': ' + self.body[:50] + '...'
