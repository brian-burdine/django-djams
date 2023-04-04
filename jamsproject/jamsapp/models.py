from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name