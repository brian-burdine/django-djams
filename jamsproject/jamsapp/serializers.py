from rest_framework import serializers
from .models import Album, Artist, Genre, Playlist, Song

class GenreBasicReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class GenreReadWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class AlbumBasicReadSerializer(serializers.HyperlinkedModelSerializer):
    genres = GenreBasicReadSerializer(many=True)
    class Meta:
        model = Album
        fields = ['name', 'genres', 'url']

class AlbumDetailedReadSerializer(serializers.ModelSerializer):
    genres = GenreBasicReadSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'publish_date', 'cover_art', 'genres']

class AlbumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'publish_date', 'cover_art', 'genres']

class ArtistBasicReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'url']

class ArtistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image', 'songs']

class SongBasicReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name']

class SongWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['name', 'length', 'artists', 'album']

class ArtistDetailedReadSerializer(serializers.ModelSerializer):
    songs = SongBasicReadSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'image', 'songs']

class SongDetailedReadSerializer(serializers.ModelSerializer):
    artists = ArtistBasicReadSerializer(many=True)
    album = AlbumBasicReadSerializer()
    class Meta:
        model = Song
        fields = ['id', 'name', 'length', 'artists', 'album']

class PlaylistReadOnlySerializer(serializers.ModelSerializer):
    songs = SongDetailedReadSerializer(many=True)
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']

class PlaylistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name', 'songs']