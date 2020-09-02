from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from rest_framework import viewsets
from .serializers import BlogSerializers
from .models import Blog
from .blog import BlogForm
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogPageView(CreateView):     #for displaying forms on blog.html
    form_class = BlogForm
    success_url = reverse_lazy('home')
    template_name = 'blog.html'


class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializers

