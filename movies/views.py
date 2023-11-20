from rest_framework import generics
from movies.models import *
from movies.serializers import *


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
