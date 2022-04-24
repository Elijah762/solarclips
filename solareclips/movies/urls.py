from django.urls import path, include
from .views import HomePageView, MoviePageView, MovieDetailView, AboutView, MovieMorePageView
from tickets.views import ReservationView
urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('movie/', MoviePageView.as_view(), name='movies'),
   path('movie/more', MovieMorePageView.as_view(), name='more'),
  path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
  path('movie/<int:pk>/ticket/', include('tickets.urls')),
  path('about-us/', AboutView.as_view(), name='about'),
  path('reservation/', ReservationView.as_view(), name='reservation')
]