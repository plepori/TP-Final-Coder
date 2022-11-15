
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View  
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post

#@login_required
def index(request):
    return render(request, 'blog/index.html')

class PostList(LoginRequiredMixin, ListView):
  model = Post

class PostCrear(CreateView):
    model = Post
    success_url = "/blog"
    fields = ['titulo', 'resumen', 'contenido', 'autor', 'imagen']

class DetailPost(DetailView):
    model=Post

class PostBorrar(DeleteView):
  model = Post
  success_url = "/blog"


class PostActualizar(UpdateView):
  model = Post
  success_url = "/blog"
  fields = ['titulo', 'resumen', 'contenido', 'autor', 'imagen']


class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("index-blog")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'


class SearchPostByName(LoginRequiredMixin, ListView):
  def get_queryset(self): 
      blog_title = self.request.GET.get('titulo')
      return Post.objects.filter(titulo__icontains=blog_title)


