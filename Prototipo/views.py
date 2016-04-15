from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from Prototipo.forms import PostForm
from Prototipo.forms import SismoForm
from Prototipo.forms import UploadFileForm
from .models import Post
from .models import Sismo


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Prototipo/post_list.html', {'posts': posts})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'Prototipo/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.published_date = timezone.now()
          post.save()
          return redirect('Prototipo.views.post_detail', pk=post.pk)

    else:
         form = PostForm()
    return render(request, 'prototipo/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('Prototipo.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'prototipo/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('Prototipo.views.post_list')


def sismos_list(request):
    sismos = Sismo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Prototipo/sismos_list.html', {'sismos': sismos})

def sismo_detail(request, pk):
        sismo = get_object_or_404(Sismo, pk=pk)
        return render(request, 'Prototipo/sismos_list.html', {'sismo': sismo})

def sismo_new(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
          sismo = form.save(commit=False)
          sismo.author = request.user
          sismo.published_date = timezone.now()
          sismo.text = 'asdf'
          sismo.save()
          return redirect('Prototipo.views.sismos_list')

    else:
         form = UploadFileForm()
    return render(request, 'prototipo/sismo_edit.html', {'form': form})


def sismo_edit(request, pk):
    sismo = get_object_or_404(Sismo, pk=pk)
    if request.method == "POST":
        form = SismoForm(request.POST, instance=sismo)
        if form.is_valid():
            sismo = form.save(commit=False)
            sismo.author = request.user
            sismo.save()
            return redirect('Prototipo.views.sismos_list')
    else:
        form = SismoForm(instance=sismo)
    return render(request, 'prototipo/sismo_edit.html', {'form': form})

def sismo_remove(request, pk):
    sismo = get_object_or_404(Sismo, pk=pk)
    sismo.delete()
    return redirect('Prototipo.views.sismos_list')