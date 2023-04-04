from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Album, Artist, Genre, Playlist, Song
from .serializers import (
    AlbumSerializer,
    ArtistSerializer,
    GenreSerializer,
    PlaylistSerializer,
    SongSerializer
)

# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer