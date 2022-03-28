from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewsArticle


class NewsList(ListView):
    model = NewsArticle
    ordering = '-news_data'
    template_name = 'articles.html'
    context_object_name = 'articles'


class NewsDetail(DetailView):
    model = NewsArticle
    template_name = 'article.html'
    context_object_name = 'article'
