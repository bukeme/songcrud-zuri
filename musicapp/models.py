from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.

class Artiste(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	age = models.IntegerField()


class Song(models.Model):
	title = models.CharField(max_length=200)
	date_released = models.DateTimeField()
	likes = models.ManyToManyField(User, blank=True)
	artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyrics(models.Model):
	content = models.TextField()
	song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
