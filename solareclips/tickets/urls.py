from django.urls import path
from .views import ReservationView, TicketView

urlpatterns = [
  path('', TicketView.as_view(), name='ticket'),
  
]