from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})

def detalhe(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return render(request,'blog/not_found.html', {'blog_id': blog_id})
    return render(request, 'blog/detalhe.html', {'blog': blog})
