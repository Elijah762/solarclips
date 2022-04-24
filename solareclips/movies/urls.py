from django.urls import path, include
from .views import HomePageView, MoviePageView, MovieDetailView, AboutView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('movie/', MoviePageView.as_view(), name='movies'),
  path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
  path('movie/<int:pk>/ticket/', include('tickets.urls')),
  path('about-us', AboutView.as_view(), name='about'),
]