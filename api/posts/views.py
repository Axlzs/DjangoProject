from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') # order by newest first date
    return render(request, 'posts/posts_list.html',{'posts':posts})

def post_page(request,slug):
    post = Post.objects.get(slug=slug) # get a specific post by slug
    return render(request, 'posts/post_page.html',{'post':post})
    
@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES) # FILES for sending an image file 
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save(   )
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form':form })

