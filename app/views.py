from django.shortcuts import render
from .forms import add_post_form
from .models import Post
from django.views.generic import CreateView, ListView, UpdateView
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ('title', 'content')


class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = ('title', 'content')
