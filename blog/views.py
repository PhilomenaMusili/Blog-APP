from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostCreateForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    title = 'list'
    context = {
        'posts':posts,
        'title':title

    }
    return render(request, 'index.html', context )

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    title = 'Detail'
    context = {
        'post':post,
        'title':title
    }
    return render(request, 'detail.html', context)
