from django.shortcuts import render, get_object_or_404
from .models import Blog
# from . import utils

# Create your views here.

def blogs(request):
    blog_list = Blog.objects.all()
    context = {
        "blog_list": blog_list,
    }
    return render(request, 'allBlog.html', context)

def blog_post_details(request, slug):
    post = Blog.objects.filter(title__startswith = slug)
    context = {
        'post' : post
    }
    return render(request, 'title.html', context)