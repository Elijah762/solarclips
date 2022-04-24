from email import message
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.CharField(max_length=500)
  rating = models.SmallIntegerField()

class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.CharField(max_length=500)

class Chat(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  chat = models.ForeignKey(Message, on_delete=models.CASCADE)


# Create your models here.
