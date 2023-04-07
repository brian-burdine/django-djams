from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Album, Artist, Genre, Playlist, Song
from .serializers import (
    AlbumReadOnlySerializer,
    AlbumWriteSerializer,
    ArtistReadOnlySerializer,
    ArtistWriteSerializer,
    GenreSerializer,
    PlaylistReadOnlySerializer,
    PlaylistWriteSerializer,
    SongReadOnlySerializer,
    SongWriteSerializer
)

# Create your views here.
write_actions = ["create", "update", "partial_update", "destroy"]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    
    def get_serializer_class(self):
        if self.action in write_actions:
            return AlbumWriteSerializer
        
        return AlbumReadOnlySerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    
    def get_serializer_class(self):
        if self.action in write_actions:
            return ArtistWriteSerializer
        
        return ArtistReadOnlySerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    
    def get_serializer_class(self):
        if self.action in write_actions:
            return PlaylistWriteSerializer
        
        return PlaylistReadOnlySerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    
    def get_serializer_class(self):
        if self.action in write_actions:
            return SongWriteSerializer
        
        return SongReadOnlySerializer