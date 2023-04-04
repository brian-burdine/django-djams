from django.contrib import admin
from .models import Album, Artist, Genre, Playlist, Song

# Register your models here.
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Playlist)