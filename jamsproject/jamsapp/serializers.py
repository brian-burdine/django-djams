from rest_framework import serializers
from .models import Album, Artist, Genre, Playlist, Song

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

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
    #songs = SongReadOnlySerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image', 'songs']

class ArtistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image', 'songs']

class SongReadOnlySerializer(serializers.ModelSerializer):
    artists = ArtistReadOnlySerializer(many=True)
    album = AlbumReadOnlySerializer()
    class Meta:
        model = Song
        fields = ['id', 'name', 'length', 'artists', 'album']

class SongWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['name', 'length', 'artists', 'album']

class PlaylistReadOnlySerializer(serializers.ModelSerializer):
    songs = SongReadOnlySerializer(many=True)
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']

class PlaylistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name', 'songs']