from rest_framework import serializers
from .models import Album, Artist, Genre, Playlist, Song

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'length', 'album']

class AlbumReadOnlySerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'publish_date', 'cover_art', 'genres']

class AlbumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'publish_date', 'cover_art', 'genres']

class ArtistReadOnlySerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image', 'songs']

class ArtistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image', 'songs']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name']
