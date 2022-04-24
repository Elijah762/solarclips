from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name = 'home_example.html'

class MoviePageView(TemplateView):
  template_name = 'browse_example.html'

class MovieDetailView(TemplateView):
  template_name = 'movie_detail_example.html'
# Create your views here.
