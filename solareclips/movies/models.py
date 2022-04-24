from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

'''''
ESRB_RATING = (
  ('G', 'General audiences'),
  ('PG', 'Parental guidance'),
  ('PG-13', 'Parents strongly cautioned'),
  ('R', 'Restricted')
)
'''''
class Movie(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=350)
  esrb = models.CharField(max_length=5)
  cover = models.ImageField(null=True, upload_to='images')
  director = models.CharField(max_length=50)
  starring = models.CharField(max_length=200)
 

  def __str__(self):
    return self.title
  
  def get_absolute_path(self):
    return reverse("movie_detail", kwargs={"pk": self.pk})

# Create your models here.