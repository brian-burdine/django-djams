from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Genre
from .serializers import (
    GenreSerializer
)

# Create your views here.
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer