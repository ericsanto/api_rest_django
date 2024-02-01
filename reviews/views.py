from django.shortcuts import render
from reviews.models import *
from reviews.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


class ReviewCreateListView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=({'message': 'Review Criado com sucesso!'}, serializer.data), status=status.HTTP_201_CREATED, headers=headers)


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Review deletado com sucesso!'})
