from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostCreateForm
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts} )

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
      form = PostCreateForm()
    return render(request, 'create.html', {'form':form})

def update_post(request, id):
    post = get_object_or_404(Post, id=id) #Toget specific task
    if request.method == 'POST': #check if user request is post
        form = PostCreateForm(request.POST, instance=post) #call form if true
        if form.is_valid():
          form.save()
          return redirect('list')
    else:
        form = PostCreateForm(instance=post)
    return render(request, 'update.html', {'form' :form})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id) #Toget specific task to delete
    if request.method == 'POST': #check if user request is post
          post.delete()         
          return redirect('list')
   
    return render(request, 'delete.html', {'post' :post})
    
