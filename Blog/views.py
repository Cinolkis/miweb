from django.shortcuts import render
from Blog.models import Post, Categoria

# Create your views here.

def blog(request):

    post= Post.objects.all()
    return render(request, "Blog/blog.html",{"posts": post})

def categoria(request, categoria_id):

    categoria= Categoria.objects.get(id=categoria_id)
    post= Post.objects.all()
    return render(request, "Blog/categoria.html",{"categoria": categoria,"posts": post})
