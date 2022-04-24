from django.contrib import admin
from .models import Room, Ticket, Showing, Food, Order

admin.site.register(Room)
admin.site.register(Ticket)
admin.site.register(Showing)
admin.site.register(Food)
admin.site.register(Order)

# Register your models here.
