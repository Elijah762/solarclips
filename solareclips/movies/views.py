from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Movie

class HomePageView(ListView):
  model = Movie
  template_name = 'home.html'

class MoviePageView(TemplateView):
  model = Movie
  template_name = 'browse_example.html'

class MovieDetailView(TemplateView):
  model = Movie
  template_name = 'movie_detail_example.html'

class AboutView(TemplateView):
  template_name = 'about.html'
# Create your views here.
