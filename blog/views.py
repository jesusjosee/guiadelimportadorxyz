from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home_blog_list(request):
    posts = Post.published.all()

    return render(request, 'blog/index_blog_list.html', {'posts': posts})

def blog_detail(request, year, month, day , post):
    post = get_object_or_404(Post, slug=post, status='published' ,publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/blog_detail.html', {'post': post})

#def blog_detail(request, id):
#    post= get_object_or_404(Post, id=id) #enviar al template el objeto recuperado 
#    return render(request, 'blog/blog_detail.html', {'post':post})