from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Blog, Comment


# Create your views here.
def view_blog(request):
    blog_elements = Blog.objects.all()
    return render(request, "blog.html", {"blog_elements": blog_elements})


def article_detail(request, slug):
    articles = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(post=articles)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            model_instance = comment_form.save(commit=False)
            model_instance.post = articles
            model_instance.author = request.user
            model_instance.save()
            return redirect("articles:view_blog")
    else:
        comment_form = CommentForm()

    return render(request, "article.html", {"articles": articles, "comments": comments, "comment_form": comment_form})


def add_comment(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect("articles:view_blog")
