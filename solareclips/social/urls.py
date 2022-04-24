from django.urls import path, include
from .views import SocialPageView

urlpatterns = [
  path('', SocialPageView.as_view(), name='social'),
]