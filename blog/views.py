from django.shortcuts import render
from .models import Blog


# Create your views here.
def view_blog(request):
    blog_elements = Blog.objects.all()
    return render(request, "blog.html", {"blog_elements": blog_elements})
