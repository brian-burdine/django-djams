from django.db import models
from datetime import date

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=500)
    length = models.DurationField()
    album = models.ForeignKey('Album', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=500)
    publish_date = models.DateField(default=date.today)
    cover_art = models.URLField(blank=True)
    genres = models.ManyToManyField('Genre', related_name='albums', related_query_name='album')

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)
    songs = models.ManyToManyField('Song', related_name='artists', related_query_name='artist')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name