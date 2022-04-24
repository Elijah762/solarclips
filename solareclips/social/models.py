from email import message
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

class Review(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.CharField(max_length=500)
  rating = models.SmallIntegerField()
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.CharField(max_length=500)


# Create your models here.
