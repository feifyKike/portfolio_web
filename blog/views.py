from django.shortcuts import render
from blog.models import Category, Post, Comment

from .forms import CommentForm
# Create your views here.


def blog_index(request):
    """Showing the posts and some categories"""
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/blog_index.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(id=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/blog_detail.html", context)
