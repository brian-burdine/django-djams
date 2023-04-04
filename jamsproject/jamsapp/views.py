from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Artist, Genre, Playlist
from .serializers import (
    ArtistSerializer,
    GenreSerializer,
    PlaylistSerializer
)

# Create your views here.
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer