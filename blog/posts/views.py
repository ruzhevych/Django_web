from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.core.files.storage import default_storage
 
# Create your views here.
def news_list(request):
    posts = Post.objects.all()
    return render(request, "posts_list.html", {'posts': posts})
# Створення нового посту
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user      
            post.save()   
            return redirect('posts:list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


# Видалення посту
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.image:
        old_image_path = os.path.join(settings.MEDIA_ROOT, post.image.name)
        if os.path.exists(old_image_path):
            os.remove(old_image_path)
    post.delete()
    return redirect('posts:list')