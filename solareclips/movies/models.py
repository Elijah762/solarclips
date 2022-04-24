from django.db import models
from django.urls import reverse


class Movie(models.Model):
  title = models.CharField(max_length=100)

  def __str__(self):
    return self.title
  
  def get_absolute_path(self):
    return reverse("movie_detail", kwargs={"pk": self.pk})

# Create your models here.