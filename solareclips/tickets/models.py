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


# Create your models here.
