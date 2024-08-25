from django.shortcuts import render, get_object_or_404,redirect
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

def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
      form = PostCreateForm()
    title = 'Create'
    context = {
        'form':form,
        'title':title
    }
    return render(request, 'create.html', context)

def update_post(request, id):
    post = get_object_or_404(Post, id=id) #Toget specific task
    if request.method == 'POST': #check if user request is post
        form = PostCreateForm(request.POST, instance=post) #call form if true
        if form.is_valid():
          form.save()
          return redirect('list')
    else:
        form = PostCreateForm(instance=post)
    title = 'Update'
    context = {
        'form':form,
        'title':title
    }
    return render(request, 'update.html', context)

def delete_post(request, id):
    post = get_object_or_404(Post, id=id) #Toget specific task to delete
    if request.method == 'POST': #check if user request is post
          post.delete()         
          return redirect('list')
    title = 'Delete'
    context = {
        'post' :post,
        'title':title
    }
    return render(request, 'delete.html', context)
    
