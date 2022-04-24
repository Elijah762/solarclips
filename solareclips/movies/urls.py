from django.urls import path
from .views import HomePageView, MoviePageView, MovieDetailView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('movie/', MoviePageView.as_view(), name='movies'),
  path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail')
]