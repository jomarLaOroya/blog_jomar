from django.shortcuts import render
from blog.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset)).distinct()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)    
    return render(request, 'index.html',{'posts':posts})

def juegos_florales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Juegos Florales'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset),
            estado = True, categoria = Categoria.objects.get(nombre = 'Juegos Florales')
            ).distinct()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'juegos_florales.html', {'posts':posts})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Generales'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset),
            estado = True, categoria = Categoria.objects.get(nombre = 'Generales')
            ).distinct()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'generales.html', {'posts':posts})

def concursos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Concursos'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset),
            estado = True, categoria = Categoria.objects.get(nombre = 'Concursos')
            ).distinct()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'concursos.html', {'posts':posts})

def ferias_escolares(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Ferias Escolares'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset),
            estado = True, categoria = Categoria.objects.get(nombre = 'Ferias Escolares')
            ).distinct()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'ferias_escolares.html', {'posts':posts})

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'post':post})