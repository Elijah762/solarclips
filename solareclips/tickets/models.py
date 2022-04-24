from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from django.db import models
from movies.models import Movie
from django.contrib.auth.models import User
import uuid


class Room(models.Model):
  room_num = models.PositiveIntegerField()

  def __str__(self):
    return str(self.room_num)


class Showing(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  time = models.DateTimeField()
  room = models.ForeignKey(Room, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.movie)


class Ticket(models.Model):
  tick_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  show = models.ForeignKey(Showing, on_delete=models.CASCADE)

  def __str__(self):
    return 'Ticket ID: ' + str(self.tick_id)

class Food(models.Model):
  name = models.CharField(max_length=50)
  picture = models.ImageField(null=True, upload_to='images/')
  price = models.DecimalField(max_digits=6, decimal_places=2)
  stock = models.PositiveIntegerField()

class Order(models.Model):
  tick = models.ForeignKey(Ticket, on_delete=models.CASCADE)
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()



# Create your models here.
