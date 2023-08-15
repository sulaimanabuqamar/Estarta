from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
# Create your views here.

def blog_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, "blog_list.html", context)

def blog_detail(request, post_id):
    each_post = Post.objects.get(post_id=post_id)
    context = {
        'blog_detail': each_post
    }
    return render(request, "blog_detail.html", context)


def blog_delete(request , post_id) :
    each_post = Post.objects.get(post_id=post_id)
    each_post.delete()
    return HttpResponseRedirect("/blog/posts/")