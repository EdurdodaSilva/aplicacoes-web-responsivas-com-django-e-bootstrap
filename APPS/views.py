from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'APPS/home.html', context)



def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'APPS/post_detail.html', context)

def blog(request):
    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'APPS/blog.html', context)
