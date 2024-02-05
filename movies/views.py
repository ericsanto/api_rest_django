from rest_framework import generics
from movies.models import *
from movies.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=({'message': 'Filme criado com Sucesso'}, serializer.data), status=status.HTTP_201_CREATED, headers=headers)


class MovieRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Filme deletador com sucesso'})
