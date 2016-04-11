from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404
from .models import *

def index(request):
    all_category = Category.objects.all()
    return render_to_response('blog/index.html', {'all_category': all_category})

def category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404('Not category')

    posts = Post.objects.filter(post_category=id)
    return render_to_response('blog/category.html', {'posts': posts})

def post(request, id_category, id):
    post = get_object_or_404(Post, id=id, post_category=id_category)
    return render_to_response('blog/post.html', {'post': post})