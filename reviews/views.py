from django.shortcuts import render
from reviews.models import *
from reviews.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ReviewCreateListView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
