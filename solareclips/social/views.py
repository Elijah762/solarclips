from django.shortcuts import render
from django.views.generic import TemplateView


class SocialPageView(TemplateView):
  template_name='social.html'
