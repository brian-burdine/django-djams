from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Genre, Playlist
from .serializers import (
    GenreSerializer,
    PlaylistSerializer
)

# Create your views here.
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer