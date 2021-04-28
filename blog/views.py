from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import Post

# Create your views here.

def register(response):
    if response.method == "post":
	    form = RegisterForm(response.post)
	    if form.is_valid():
	        form.save()

	    return redirect("/home")
    else:
	    form = RegisterForm()

    return render(response, "/blog/register.html", {"form":form})

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
