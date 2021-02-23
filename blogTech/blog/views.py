from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

# Create your views here.
def index(request):
    blogs = list(Blog.objects.order_by('-data_criacao'))
    blog_mais_recente = blogs[0]
    del blogs[0]
    return render(request, 'blog/index.html', {'blogs': blogs, 
                                               'titulo': 'Meu Blog', 
                                               'blog_mais_recente': blog_mais_recente})

def detalhe(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return render(request,'blog/not_found.html', {'blog_id': blog_id})
    return render(request, 'blog/detalhe.html', {'blog': blog})
