from rest_framework import serializers
from .models import Album, Artist, Genre, Playlist, Song

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'publish_date', 'cover_art']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'image']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['name', 'length', 'album']