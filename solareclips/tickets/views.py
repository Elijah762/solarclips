from django.shortcuts import render
from django.views.generic import TemplateView


class TicketView(TemplateView):
  template_name='ticket_example.html'

class ReservationView(TemplateView):
  template_name = 'reservation.html'
# Create your views here.
